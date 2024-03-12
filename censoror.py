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

Model = spacy.load("en_core_web_md") # Loading the English model for spaCy

def ArgParse():
    # Creating an argument parser instance
    varx = argparse.ArgumentParser(description="Censoring important and sensitive data from text documents")
    # Adding arguments to the argument parser
    varx.add_argument('--input', nargs="+", help='Input files using Glob pattern')
    varx.add_argument('--output', required=True, type=str, help='Output directory for Censored files')
    varx.add_argument('--names', action='store_true', help='Censoring Names')
    varx.add_argument('--dates', action='store_true', help='Censoring Dates')
    varx.add_argument('--phones', action='store_true', help='Censoring Phone Numbers')
    varx.add_argument('--address', action='store_true', help='Censoring Location or Address')
    varx.add_argument('--stats', type=str, help='Statistics Output Destination')
    return varx.parse_args()

def CenName(MailData):
    Mod = Model(MailData)
    # Extracting person label from the text using spaCy
    return [ent.text for ent in Mod.ents if ent.label_ == "PERSON"]
    
def CenDate(MailData):
    # Initializing Google Cloud Natural Language API 
    GoogleMod = language_v1.LanguageServiceClient.from_service_account_json('key.json')
    file = language_v1.Document(content=MailData, type_=language_v1.Document.Type.PLAIN_TEXT)
    # Analyzing entities in the text using Google Cloud Natural Language API
    response = GoogleMod.analyze_entities(document=file, encoding_type=language_v1.EncodingType.UTF8)
    x = response.entities
    # Extracting Dates from the text using Google Cloud Natural Language API 
    return [entity.name for entity in x if language_v1.Entity.Type(entity.type_).name in ["DATE"]]

def CenNum(MailData):
    # Initializing Google Cloud Natural Language API 
    GoogleMod = language_v1.LanguageServiceClient.from_service_account_json('key.json')
    file = language_v1.Document(content=MailData, type_=language_v1.Document.Type.PLAIN_TEXT)
    # Analyzing entities in the text using Google Cloud Natural Language API
    response = GoogleMod.analyze_entities(document=file, encoding_type=language_v1.EncodingType.UTF8)
    x = response.entities
    # Extracting Phone Numbers from the text using Google Cloud Natural Language API 
    return [entity.name for entity in x if language_v1.Entity.Type(entity.type_).name in ["PHONE_NUMBER"]]

def CenLoc(MailData):
    # Initializing Google Cloud Natural Language API 
    GoogleMod = language_v1.LanguageServiceClient.from_service_account_json('key.json')
    file = language_v1.Document(content=MailData, type_=language_v1.Document.Type.PLAIN_TEXT)
    # Analyzing entities in the text using Google Cloud Natural Language API
    response = GoogleMod.analyze_entities(document=file, encoding_type=language_v1.EncodingType.UTF8)
    x = response.entities
    # Extracting Address from the text using Google Cloud Natural Language API 
    return [entity.name for entity in x if language_v1.Entity.Type(entity.type_).name in ["ADDRESS"]]

def analyze_entities(MailData, FlaTyp):
    # Analyzing entities in the provided text using spaCy and Google Cloud Natural Language API
    y=[] # calculating the number of entity flags
    stat = [] #Calculating stats 

    # Counting occurrences of different types of entity flags 
    if FlaTyp['names']: 
            var1= CenName(MailData)
            y.extend(var1) # Extend the list y with the extracted names
            stat.append(len(var1)) 
    else: stat.append(0) # If 'names' flag is not set, append 0 to the stat list

    if FlaTyp['dates']:
            var2= CenDate(MailData)
            y.extend(var2) # Extend the list y with the extracted dates
            stat.append(len(var2))
    else: stat.append(0) # If 'dates' flag is not set, append 0 to the stat list

    if FlaTyp['phones']:
            var3= CenNum(MailData)
            y.extend(var3) # Extend the list y with the extracted phone number
            stat.append(len(var3))
    else: stat.append(0) # If 'phones' flag is not set, append 0 to the stat list

    if FlaTyp['address']:
            var4= CenLoc(MailData)
            y.extend(var4) # Extend the list y with the extracted addresses 
            stat.append(len(var4))
    else: stat.append(0) # If 'address' flag is not set, append 0 to the stat list

    return y, stat

def censor(info, type):
    # Censoring sensitive information in the provided text
    temp = case(type)
    for x in temp:
        code = "\u2588" * len(x)  # Unicode character to censor sensitive data
        info = info.replace(x, code)  
    return info

def CenP(data, FlaTyp):
    # Censoring sensitive information in the provided text
    x, stat= analyze_entities(data, FlaTyp) # Calling analyze_entites to check flag inputted 
    data = censor(data, x) # Call censor function to censor sensitive data with Block character 
    # Printing statistics of censored flags
    NewArg =ArgParse()
    if NewArg.stats=='stdout' or  NewArg.stats=='stderr': # Printing statistics of censored flags in stderr or stdout
        print ("Censored Names:",stat[0], " Censored Date:", stat[1], " Censored Phone Numbers:", stat[2], " Censored Addresses:", stat[3])
    else: 
        Censored_Statistics=NewArg.stats #Printing statistics of censored flags in .txt files format
        with open(Censored_Statistics, "a", encoding="utf-8") as x:
             x.write(f'Censored Names: {stat[0]}   Censored Date: {stat[1]}   Censored Phone Numbers: {stat[2]}   Censored Addresses: {stat[3]}\n')
    return data

def case(x):
    # Filtering out elements not matching the specified pattern
    return [temp for temp in x if not re.match(r"^\d{4}$", temp)]

def Read(Xtemp, CCd, FlaTyp):
    # Reading input files, censoring sensitive information, and writing censored files
    for x in Xtemp:
        try:
            with open(x, "r", encoding="utf-8") as file:
                data = file.read()

            censored = CenP(data, FlaTyp)  # Censoring sensitive information in the text
            New = os.path.basename(x) + '.censored'
            Odir = os.path.join(CCd, New)
            os.makedirs(CCd, exist_ok=True)
            with open(Odir, 'w',encoding='utf-8') as newfile:
                newfile.write(censored)  # Writing censored text to a new file
        except Exception as e:
            print(f'Error Reading file {x}: {e}')  # Handling errors while reading files

def main():
    # Main function for handling program execution
    tem = ArgParse()
    if not tem.input:
        print('Error!! Please give input file')  # Prompting user to provide input files
    else:
        list = []
        for x in tem.input:
            list.extend(glob.glob(os.path.join('./', x)))  # Finding files matching the provided patterns

        if not list:
            print('Error!! Specific extension file not found')  # Alerting user if specified files are not found
        else:
            os.makedirs(tem.output, exist_ok=True)  # Creating the output directory if it doesn't exist

            temp = {"names": tem.names, "dates": tem.dates, "phones": tem.phones, "address": tem.address}
            SFlag = [flag for flag, value in temp.items() if value]

            if SFlag:
                Read(list, tem.output, temp)  # Reading and censoring files if censoring flags are specified
            else:
                print("Error!! Mention some Censor flag (no less than 1)!")  # Prompting user to specify censoring flags

if __name__ == "__main__":
    main()  
