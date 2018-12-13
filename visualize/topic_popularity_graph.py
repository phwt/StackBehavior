""" StackBehavior - User Chart
This module visualize user count by country into bar chart using pygal library
"""
import pygal
import csv

# source = './dataset/data/tag_counts/tags_count_topic_based_percentage.csv'
# source = './dataset/data/tag_counts/tags_count_topic_based_percentage_year.csv'
# output = './visualize/output/topic_popularity/test.svg'

def readPercentage(path):
    """ Read CSV containing year and percentage
        Arguments:
            `path` - Input file's path (string)
        Return:
            A list of every row read from `path` file
            Sample - [(2008, 40), (2009, 2029)...(2018, 99904)]
    """
    with open(path, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # for i in readCSV:
            # print(i)
        print([[i[0] for i in readCSV], [i[1] for i in readCSV]])
    # return data_out

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

def visualizeSingle(source, output):
    readInt(source)

print(readPercentage('./dataset/data/tag_counts/topic_based_percentage/TAGS_APACHE_P.csv'))

# visualize()
# getTopics()
# read()
