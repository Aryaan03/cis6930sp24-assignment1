import argparse
import glob
import os
import re
import sys
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_lg")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Censor sensitive information from text files.")
    parser.add_argument('--input', type=str, action='append', help='Glob pattern for input files')
    parser.add_argument('--output', type=str, help='Directory to store censored files')
    parser.add_argument('--names', action='store_true', help='Censor names')
    parser.add_argument('--dates', action='store_true', help='Censor dates')
    parser.add_argument('--phones', action='store_true', help='Censor phone numbers')
    parser.add_argument('--address', action='store_true', help='Censor physical addresses')
    parser.add_argument('--stats', type=str, help='File or location to write statistics')
    return parser.parse_args()

def expand_globs(glob_patterns):
    file_paths = []
    for pattern in glob_patterns:
        file_paths.extend(glob.glob(pattern))
    return file_paths

def censor_dates(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "DATE":
            text = text.replace(ent.text, "█"*len(ent.text))
    return text

def censor_phone_numbers(text):
    phone_pattern = r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$'
    return re.sub(phone_pattern, '█', text)

def censor_names_with_spacy(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            text = text.replace(ent.text, "█"*len(ent.text))
    return text

def censor_addresses_with_spacy(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC", "FAC"]:
            text = text.replace(ent.text, "█"*len(ent.text))
    return text

def censor_content(content, censor_flags):
    stats = {'dates': 0, 'phones': 0, 'names': 0, 'addresses': 0}
    if censor_flags['dates']:
        content = censor_dates(content)
    if censor_flags['phones']:
        content = censor_phone_numbers(content)
    if censor_flags['names']:
        content = censor_names_with_spacy(content)
    if censor_flags['address']:
        content = censor_addresses_with_spacy(content)
    return content, stats

def read_and_censor_file(file_path, censor_flags):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        censored_content, stats = censor_content(content, censor_flags)
        return censored_content, stats

def write_censored_file(original_path, censored_content, output_dir):
    base_name = os.path.basename(original_path)
    censored_file_path = os.path.join(output_dir, f"{base_name}.censored")
    with open(censored_file_path, 'w', encoding='utf-8') as censored_file:
        censored_file.write(censored_content)

def write_statistics(stats, stats_output):
    if stats_output in ['stderr', 'stdout']:
        output_stream = getattr(sys, stats_output)
        output_stream.write(str(stats) + '\n')
    else:
        with open(stats_output, 'w', encoding='utf-8') as stats_file:
            stats_file.write(str(stats) + '\n')

def process_files(file_paths, censor_flags, output_dir, stats_output):
    overall_stats = {'dates': 0, 'phones': 0, 'names': 0, 'addresses': 0}
    for file_path in file_paths:
        censored_content, file_stats = read_and_censor_file(file_path, censor_flags)
        for key in overall_stats:
            overall_stats[key] += file_stats[key]
        write_censored_file(file_path, censored_content, output_dir)
    write_statistics(overall_stats, stats_output)

if __name__ == "__main__":
    args = parse_arguments()
    file_paths = expand_globs(args.input)
    censor_flags = {
        'names': args.names,
        'dates': args.dates,
        'phones': args.phones,
        'address': args.address
    }
    process_files(file_paths, censor_flags, args.output, args.stats)