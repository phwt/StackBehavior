""" StackBehavior - Tags Count Compare
This module is for comparing tags count with total questions asked in percentage.
"""
import csv
global question_count
question_count = list()

def readFile():
    """ Read the given csv file """
    getCount()
    path = './dataset/data/tag_counts/tags_count_topic_based_merged.csv'
    with open(path, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # next(readCSV, None) #Skip header
        for row in readCSV:
            compare(row)
            # print(row)

def getCount():
    """ Read 'question_count_by_year_quarter.csv' and store """
    path = './dataset/data/question_count_by_year_quarter.csv'
    with open(path, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV, None) #Skip header
        for row in readCSV:
            question_count.append(list(map(int, row)))

def compare(topics):
    """ Compare topic count with question count """
    year, quarter, topic, count = int(topics[0]), int(topics[1]), topics[2], int(topics[3])
    for i in question_count:
        # print(i[:-1])
        # print([year, quarter])
        if i[:-1] == [year, quarter]:
            percentage = (count/i[2])*100
            write_file(year, quarter, topic, count, percentage)
            print(i[2])
            return

def write_file(year, quarter, topic, count, percentage):
    """ Write data from csv reader """
    with open('./dataset/data/tag_counts/tags_count_topic_based_percentage.csv', 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([year, quarter, topic, count, percentage])
    csvfile.close()
readFile()
# getCount()
# print(question_count)
# compare([2018, 1, "haha", 123])

