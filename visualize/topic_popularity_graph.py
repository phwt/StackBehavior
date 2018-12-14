""" StackBehavior - Topic Popularity Graph
Visualize each topic popularity data into line graph format.
"""
import pygal
import csv

def readConvert(path):
    """ Read and convert data into two list year and popularity percentage
        Arguements:
            `path` - Input file's path (string)
        Return:
            Two seperated list
    """
    with open(path, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        readCSV = [[int(i[0]), float(i[1])] for i in readCSV]
        return list(zip(*readCSV))

def visualize(title, data, output):
    line_chart = pygal.Line(height=300, show_legend=False)
    line_chart.title = title
    line_chart.x_labels = data[0]
    line_chart.add('', data[1])
    line_chart.render_to_file(output)

def visualizeSingle(title, data, output):
    data = readConvert(data)
    visualize("Python", data, output)

# Below this line is for debugging purpose only
# visualizeSingle("Python", "./dataset/data/tag_counts/topic_based_percentage/TAGS_PYTHON_P.csv",
# "./visualize/output/topic_popularity/python.svg")