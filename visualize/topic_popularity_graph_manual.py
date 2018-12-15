""" StackBehavior - Topic Popularity Graph Manual
Visualize selectedtopic popularity data into line graph format manually.
"""
import pygal
import csv

def visualize(title, output):
    """ Visualize the given data into line graph and render to file
        Arguements:
            `title` - Graph's title (string)
            `data` - Graph's data (list)
            `output` - Output file's path (string)
            `file_format` - Output file's format (`PNG` of `SVG`(default))
        Return: None
        Output: Vector Graphic (.svg) file
    """
    line_chart = pygal.Line(height=300, show_legend=True)
    line_chart.title = title
    line_chart.x_labels = [i for i in range(2008, 2018+1)]

    line_chart.add('Eclipse', [0.9413, 0.789, 0.9115, 1.0114, 1.1009, 0.9966, 1.0991, 0.7613, 0.5591, 0.4673, 0.3772])
    line_chart.add('Android Studio', [None, None, None, 0.0003, 0.0002, 0.0891, 0.1988, 0.4765, 0.6658, 0.4769, 0.6002])
    line_chart.render_to_file(output)

visualize("Eclipse and Android Studio", "./visualize/output/topic_popularity/custom/ECLIPSE_ANDROID.svg")

# Below this line is for debugging purpose only
# visualizeSingle("Python", "./dataset/data/tag_counts/topic_based_percentage/TAGS_PYTHON_P.csv",
# "./visualize/output/topic_popularity/python.svg", "PNG")
