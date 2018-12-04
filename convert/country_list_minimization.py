""" StackBehavior - Country List Minimization
This module converts location name into country code that supported by pygal.

Example:
    "Bangkok, Thailand" = "th"
    "Reykjavik" = "is"

"""
import csv
# import json
# import requests
from progress.bar import IncrementalBar

data_dict = {}
# source, output = './dataset/data/user_location_raw.csv', './dataset/data/user_location_min.csv'
source, output = './dataset/data/reputation_raw.csv', './dataset/data/reputation_min.csv'

# def check_geo(txt):
    # """ Further check for country name using Google Geocoding """
    # url = "https://maps.googleapis.com/maps/api/geocode/json?address="+txt+"&key=" #Not Used anymore
    # return requests.get(url).json()['results'][0]['address_components'][-1]['short_name'].lower()

def check(txt):
    """ Check if the input country name match any data in 'pygal_supported_country.csv' or not """
    with open('./dataset/data/pygal_supported_country.csv', encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[1].lower() in txt.lower():
                return row[0]
        return None

def read():
    """ Read 'user_location_raw.csv' file """
    with open(source, encoding="utf8") as csvfile:
        row_count = sum(1 for row in csvfile)
    bar = IncrementalBar('Reading', max=row_count)
    with open(source, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if check(row[0]) != None:
                add_dict([check(row[0]), row[1]])
            bar.next()
    bar.finish()
    write_file()

def add_dict(data):
    """ Add item to dict """
    try:
        data_dict[data[0]] += int(data[1])
    except KeyError:
        data_dict[data[0]] = int(data[1])

def write_file():
    """ Write data_dict to file """
    bar = IncrementalBar('Writing', max=len(data_dict))
    with open(output, 'a', encoding="utf8", newline='') as csvfile:
        for i, j in data_dict.items():
            writer = csv.writer(csvfile)
            writer.writerow([i, j])
            bar.next()
    csvfile.close()
    bar.finish()
read()
