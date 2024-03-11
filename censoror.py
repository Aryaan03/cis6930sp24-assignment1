import re
import sys
import os
import argparse
import pytest
import nltk
import spacy
import glob
import snorkel
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from google.cloud import language_v1

spacy.cli.download("en_core_web_md")
Model = spacy.load("en_core_web_md")

def parg():
    varx = argparse.ArgumentParser(description="Censoring important and sensitive data from text documents")
    varx.add_argument('--input', nargs="+", help='Input files using Glob pattern')
    varx.add_argument('--output', required=True, type=str, help='Output directory for Censored files')
    varx.add_argument('--names', action='store_true', help='Censoring Names')
    varx.add_argument('--dates', action='store_true', help='Censoring Dates')
    varx.add_argument('--phones', action='store_true', help='Censoring Phone Numbers')
    varx.add_argument('--address', action='store_true', help='Censoring Location or Address')
    varx.add_argument('--stats', choices=['stdout', 'stderr'], default='stderr', help='Statistics Output Destination')
    return varx.parse_args()

def case(x):
    return [temp for temp in x if not re.match(r'^\d{4}$', temp)]

def censor(info, type):
    temp = case(type)
    for x in temp:
        code = "\u2588" * len(x)
        info = info.replace(x, code)
    return info

def analyze_entities(MailData):
    stat = []
    Mod = Model(MailData)
    Person = [ent.text for ent in Mod.ents if ent.label_ == "PERSON"]


    GoogleMod = language_v1.LanguageServiceClient.from_service_account_json('key.json')
    file = language_v1.Document(content=MailData, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = GoogleMod.analyze_entities(document=file, encoding_type=language_v1.EncodingType.UTF8)

    x = response.entities
    verify= [entity.name for entity in x if language_v1.Entity.Type(entity.type_).name in ["PHONE_NUMBER"]]
    verify= [entity.name for entity in x if language_v1.Entity.Type(entity.type_).name in ["ADDRESS"]]
    verify= [entity.name for entity in x if language_v1.Entity.Type(entity.type_).name in ["DATE"]]

    Phone_Numbers=0
    Locations=0
    Dates=0

    for entity in x:
        if language_v1.Entity.Type(entity.type_).name == 'DATE' :
            Dates += 1
        elif language_v1.Entity.Type(entity.type_).name == "PHONE_NUMBER" :
            Phone_Numbers += 1
        elif language_v1.Entity.Type(entity.type_).name == "ADDRESS" :
            Locations += 1


    stat = [Dates, Phone_Numbers, Locations, len(Person)]
    verify += Person     
    return verify, stat

def CenP(data):
    entities, count= analyze_entities(data)
    data = censor(data, entities)
    print ("Censored Names:",count[3], " Censored Date:", count[1], " Censored Phone Numbers:", count[2], " Censored Addresses:", count[0])
    return data

def Read(Xtemp, CCd):
    for x in Xtemp:
        try:
            with open(x, 'r', encoding="utf-8") as file:
                data = file.read()

            censored = CenP(data)
            New = os.path.basename(x) + '.censored'
            Odir = os.path.join(CCd, New)
            os.makedirs(CCd, exist_ok=True)
            with open(Odir, 'w',encoding='utf-8') as newfile:
                newfile.write(censored)
        except Exception as e:
            print(f'Error Reading file {x}: {e}')



def main():
    tem = parg()
    if not tem.input:
        print('Please give input file')
    else:
        list = []
        for x in tem.input:
            list.extend(glob.glob(os.path.join('./', x)))

        if not list:
            print('Specific extension file not found')
        else:
            os.makedirs(tem.output, exist_ok=True)

            censor_flags = {"names": tem.names, "dates": tem.dates, "phones": tem.phones, "address": tem.address}
            selected_flags = [flag for flag, value in censor_flags.items() if value]

            if selected_flags:
                Read(list, tem.output)
            else:
                print("Mention some Censor flag")

if __name__ == "__main__":
    main()
