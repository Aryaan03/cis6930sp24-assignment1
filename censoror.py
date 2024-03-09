import re
import sys
import os
import argparse
import pytest
import nltk
import spacy
import glob

Model = spacy.load("en_core_web_md")



def CenName(data):
    Mod = Model(data)
    for x in Mod.ents:
        if x.label_ == "PERSON":
            data = data.replace(x.text, "█" * len(x.text))
    return data

def CenDate(data):
    Mods = Model(data)
    for x in Mods.ents:
        if x.label_ == "DATE":
            data = data.replace(x.text, "█" * len(x.text))
    return data

def CenNum(data):
    NumPat = re.findall(r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$', data)
    for x in NumPat:
        data = data.replace(x, '█' * len(x))
    return data

def CenLoc(data):
    Mods = Model(data)
    for x in Mods.ents:
        if x.label_ == "GPE" or x.label_ == "LOC" or x.label_ == "FAC":
            data = data.replace(x.text, "█"*len(x.text))
    return data

def CenInf(dat, temp):
    Statistics = {'names': 0, 'dates': 0, 'phones': 0, 'addresses': 0}
    if temp['names']:
        dat = CenName(dat)
    if temp['dates']:
        dat = CenDate(dat)
    if temp['phones']:
        dat = CenNum(dat)
    if temp['addresses']:
        dat = CenLoc(dat)
    return dat, Statistics

def Input(dir, temp):
    with open(dir, 'r', encoding='utf-8') as file:
        dat = file.read()
        Ccd, Statistics = CenInf(dat, temp)
        return Ccd, Statistics

def Output(Xtemp, Ccd, Odir):
    OldN = os.path.basename(Xtemp)
    Cdir = os.path.join(Odir, f"{OldN}.censored")
    with open(Cdir, 'w', encoding='utf-8') as OldExt:
        OldExt.write(Ccd)


def parg():
    varx = argparse.ArgumentParser(description="Censoring important and sensitive data from text documents")
    varx.add_argument('--input', type=str, action='append', help='Input files using Glob pattern')
    varx.add_argument('--names', action='store_true', help='Censoring Names')
    varx.add_argument('--dates', action='store_true', help='Censoring Dates')
    varx.add_argument('--phones', action='store_true', help='Censoring Phone Numbers')
    varx.add_argument('--addresses', action='store_true', help='Censoring Location or Address')
    varx.add_argument('--output', type=str, help='Output directory for Censored files') 
    varx.add_argument('--stats', type=str, help='Statistics Output Destination')
    return varx.parse_args()

def main():
    args = parg()
    list = []
    for x in args.input:
        list.extend(glob.glob(x))

    temp = {
        'names': args.names,
        'dates': args.dates,
        'phones': args.phones,
        'addresses': args.addresses
    }

    Show = {'names': 0, 'phones': 0, 'dates': 0, 'addresses': 0}
    for x in args.input:
        CDat, DocSt = Input(x, temp)
        for Y in Show:
            Show[Y] += DocSt[Y]
        Output(x, CDat, args.output)
 
    if args.stats in ['stderr', 'stdout']:
        X = getattr(sys, args.stats)
        X.write(str(Show) + '\n')
    else:
        with open(args.stats, 'w', encoding='utf-8') as CountF:
            CountF.write(str(Show) + '\n')

if __name__ == "__main__":
    main()
    
