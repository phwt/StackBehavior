""" StackBehavior - User Chart
This module visualize user count by country into bar chart using pygal library
"""
import pygal
import csv

# source = './dataset/data/tag_counts/tags_count_topic_based_percentage.csv'
source = './dataset/data/tag_counts/tags_count_topic_based_percentage_year.csv'
output = './visualize/output/topic_popularity/test.svg'

def getTopics():
    """ Return a set of topics """
    topics = set()
    with open(source, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            topics.add(row[2])
    return topics

topics = getTopics()

def read():
    """ Read a file """
    time, percentage = list(), list()
    with open(source, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[1] == "ANDROID":
                time.append(row[0])
                percentage.append(float(row[3]))
    visualize("Android", time, percentage)

def visualize(title, time, percentage):
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = time
    line_chart.add('', percentage)
    line_chart.render_to_file(output)
# visualize()
# getTopics()
read()