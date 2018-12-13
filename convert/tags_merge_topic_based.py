""" StackBehavior - Tags Merge Topic Based
This module is for merging tags count(s) files into one file.
"""
import csv
import os

def readBatch():
    """ Read all files in '/dataset/data/tag_counts/topic_based' """
    rootdir = './dataset/data/tag_counts/topic_based_year'
    # rootdir = './dataset/data/tag_counts/topic_based_quarter'
    for subdir, _, files in os.walk(rootdir):
        for file in files:
            path = os.path.join(subdir, file)
            with open(path, encoding="utf8") as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                next(readCSV, None) #Skip header
                for row in readCSV:
                    write_file(row[0], path.split("_")[-1][:-4], row[1])

def write_file(year, name, count):
    """ Write data from csv reader """
    with open('./dataset/data/tag_counts/tags_count_topic_based_merged_year.csv', 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([year, name, count])
    csvfile.close()

readBatch()
