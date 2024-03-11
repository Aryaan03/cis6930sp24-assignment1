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
# Google Cloud Natural Language API

spacy.cli.download("en_core_web_md") # Downloading the English model for spaCy

Model = spacy.load("en_core_web_md") # Loading the English model for spaCy

def parg():
    # Creating an argument parser instance
    varx = argparse.ArgumentParser(description="Censoring important and sensitive data from text documents")
    # Adding arguments to the argument parser
    varx.add_argument('--input', nargs="+", help='Input files using Glob pattern')
    varx.add_argument('--output', required=True, type=str, help='Output directory for Censored files')
    varx.add_argument('--names', action='store_true', help='Censoring Names')
    varx.add_argument('--dates', action='store_true', help='Censoring Dates')
    varx.add_argument('--phones', action='store_true', help='Censoring Phone Numbers')
    varx.add_argument('--address', action='store_true', help='Censoring Location or Address')
    varx.add_argument('--stats', choices=['stdout', 'stderr'], default='stderr', help='Statistics Output Destination')
    return varx.parse_args()

def case(x):
    # Filtering out elements not matching the specified pattern
    return [temp for temp in x if not re.match(r'^\d{4}$', temp)]

def censor(info, type):
    # Censoring sensitive information in the provided text
    temp = case(type)
    for x in temp:
        code = "\u2588" * len(x)  # Unicode character to censor sensitive data
        info = info.replace(x, code)  
    return info

def analyze_entities(MailData):
    # Analyzing entities in the provided text using spaCy and Google Cloud Natural Language API
    stat = []
    Mod = Model(MailData) 

    # Extracting person label from the text using spaCy
    Person = [ent.text for ent in Mod.ents if ent.label_ == "PERSON"]

    # Initializing Google Cloud Natural Language API client
    GoogleMod = language_v1.LanguageServiceClient.from_service_account_json('key.json')
    file = language_v1.Document(content=MailData, type_=language_v1.Document.Type.PLAIN_TEXT)
    # Analyzing entities in the text using Google Cloud Natural Language API
    response = GoogleMod.analyze_entities(document=file, encoding_type=language_v1.EncodingType.UTF8)

    x = response.entities
    # Extracting phone numbers, addresses, and dates from the analyzed entities
    verify= [entity.name for entity in x if language_v1.Entity.Type(entity.type_).name in ["PHONE_NUMBER"]]
    verify= [entity.name for entity in x if language_v1.Entity.Type(entity.type_).name in ["ADDRESS"]]
    verify= [entity.name for entity in x if language_v1.Entity.Type(entity.type_).name in ["DATE"]]

    Phone_Numbers=0
    Locations=0
    Dates=0

    # Counting occurrences of different types of entities
    for entity in x:
        if language_v1.Entity.Type(entity.type_).name == 'DATE' :
            Dates += 1
        elif language_v1.Entity.Type(entity.type_).name == "PHONE_NUMBER" :
            Phone_Numbers += 1
        elif language_v1.Entity.Type(entity.type_).name == "ADDRESS" :
            Locations += 1

    stat = [Dates, Phone_Numbers, Locations, len(Person)]  
    verify += Person  # Combining detected entities and persons
    return verify, stat

def CenP(data):
    # Censoring sensitive information in the provided text
    entities, count= analyze_entities(data)
    data = censor(data, entities)
    # Printing statistics of censored flags
    print ("Censored Names:",count[3], " Censored Date:", count[1], " Censored Phone Numbers:", count[2], " Censored Addresses:", count[0])
    return data

def Read(Xtemp, CCd):
    # Reading input files, censoring sensitive information, and writing censored files
    for x in Xtemp:
        try:
            with open(x, 'r', encoding="utf-8") as file:
                data = file.read()

            censored = CenP(data)  # Censoring sensitive information in the text
            New = os.path.basename(x) + '.censored'
            Odir = os.path.join(CCd, New)
            os.makedirs(CCd, exist_ok=True)
            with open(Odir, 'w',encoding='utf-8') as newfile:
                newfile.write(censored)  # Writing censored text to a new file
        except Exception as e:
            print(f'Error Reading file {x}: {e}')  # Handling errors while reading files

def main():
    # Main function for handling program execution
    tem = parg()
    if not tem.input:
        print('Please give input file')  # Prompting user to provide input files
    else:
        list = []
        for x in tem.input:
            list.extend(glob.glob(os.path.join('./', x)))  # Finding files matching the provided patterns

        if not list:
            print('Specific extension file not found')  # Alerting user if specified files are not found
        else:
            os.makedirs(tem.output, exist_ok=True)  # Creating the output directory if it doesn't exist

            censor_flags = {"names": tem.names, "dates": tem.dates, "phones": tem.phones, "address": tem.address}
            selected_flags = [flag for flag, value in censor_flags.items() if value]

            if selected_flags:
                Read(list, tem.output)  # Reading and censoring files if censoring flags are specified
            else:
                print("Mention some Censor flag")  # Prompting user to specify censoring flags

if __name__ == "__main__":
    main()  
