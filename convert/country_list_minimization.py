""" StackBehavior - Country List Minimization
This module converts location name into country code that supported by pygal.

Example:
    "Bangkok, Thailand" = "th"
    "Reykjavik" = "is"

"""
import csv
import json
import requests

def check_geo(txt):
    """ Further check for country name using Google Geocoding """
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+txt+"&key=AIzaSyDzndgrPuhUFE_xdJmblexiYHsXWLCFyzE"
    response = requests.get(url).json()
    return response['results'][0]['formatted_address']

def check(txt):
    """ Check if the input country name match any data in 'pygal_supported_country.csv' or not """
    with open('./dataset/data/pygal_supported_country.csv', encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[1].lower() in txt.lower():
                return row[0]
        return check(check_geo(txt))

def read():
    """ Read 'user_location_raw.csv' file """
    with open('./dataset/data/user_location_raw.csv', encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row[0])

print(check("Bangkok"))
