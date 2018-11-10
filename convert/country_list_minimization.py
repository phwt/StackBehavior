""" StackBehavior - Country List Minimization
This module converts location name into country code that supported by pygal.

Example:
    "Bangkok, Thailand" = "th"
    "Reykjavik" = "is"

"""
import csv
import json
import requests
global cnt
cnt = 0

def check_geo(txt):
    """ Further check for country name using Google Geocoding """
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+txt+"&key=AIzaSyDzndgrPuhUFE_xdJmblexiYHsXWLCFyzE"
    return requests.get(url).json()['results'][0]['address_components'][-1]['short_name'].lower()

def check(txt):
    global cnt
    """ Check if the input country name match any data in 'pygal_supported_country.csv' or not """
    with open('./dataset/data/pygal_supported_country.csv', encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[1].lower() in txt.lower():
                return row[0]
        cnt += 1
        # return txt
        # return check_geo(txt)

def read():
    """ Read 'user_location_raw.csv' file """
    with open('./dataset/data/user_location_raw.csv', encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # cnt = 0
        for row in readCSV:
            check(row[0])
            # print(check(row[0]))
            # cnt += 1
            # write_file([check(row[0]), row[1]])
            # if cnt == 1000:
                # break
            # check(row[0])

def write_file(data):
    # with open('user_location_min.csv', 'a', encoding="utf8") as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(data)
    # csvfile.close()
    f = open("kwai.txt", "a")
    print(data[0]+","+data[1])
    f.write(data[0]+","+data[1])

# print(read())
read()
print(cnt)