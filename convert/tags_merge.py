""" StackBehavior - Tags Merge
This module is for merging tags count(s) files into one file.
"""
import csv
import os

def readBatch():
    """ Read all files in '/dataset/data/tag_counts' """
    rootdir = './dataset/data/tag_counts'
    for subdir, _, files in os.walk(rootdir):
        for file in files:
            path = os.path.join(subdir, file)
            with open(path, encoding="utf8") as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                next(readCSV, None)
                for row in readCSV:
                    write_file(path.split("_")[2][:-4], row[0], row[1])

def write_file(year, name, count):
    """ Write data from csv reader """
    with open('./dataset/data/tags_count_merged.csv', 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([year, name, count])
    csvfile.close()

readBatch()
