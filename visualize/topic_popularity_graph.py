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

def visualize(title, data, output, file_format):
    """ Visualize the given data into line graph and render to file
        Arguements:
            `title` - Graph's title (string)
            `data` - Graph's data (list)
            `output` - Output file's path (string)
            `file_format` - Output file's format (`PNG` of `SVG`(default))
        Return: None
        Output: Vector Graphic (.svg) file
    """
    line_chart = pygal.Line(height=300, show_legend=False)
    line_chart.title = title
    line_chart.x_labels = data[0]
    line_chart.add('', data[1])
    if file_format == "SVG":
        line_chart.render_to_file(output)
    elif file_format == "PNG":
        line_chart.render_to_png(output)

def visualizeSingle(title, data, output, file_format):
    """ Visualize data from a single file
        Arguments:
            `title` - Graph's title (string)
            `data` - Graph's data (list)
            `output` - Output file's path (string)
            `file_format` - Output file's format (`PNG` of `SVG`(default))
        Return: None
        Output: Vector Graphic (.svg) file
    """
    data = readConvert(data)
    visualize(title, data, output, file_format)

# Below this line is for debugging purpose only
# visualizeSingle("Python", "./dataset/data/tag_counts/topic_based_percentage/TAGS_PYTHON_P.csv",
# "./visualize/output/topic_popularity/python.svg", "PNG")
