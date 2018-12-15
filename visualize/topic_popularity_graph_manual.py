""" StackBehavior - Topic Popularity Graph Manual
Visualize selectedtopic popularity data into line graph format manually.
"""
import pygal
import csv
from pygal.style import Style

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
    style = Style(
        font_family='googlefont:Athiti',
        # colors=('#4B8BBE', '#FF0000', '#fdcd3e') #OOL
        # colors=('#463685', '#A4CC44') #IDE
        # colors=('#007ACC') #TXT
    )
    line_chart = pygal.Line(height=300, show_legend=True, style=style, y_title='% จากคำถามทั้งหมด',
    legend_at_bottom=True, legend_at_bottom_columns=3, max_scale=8, truncate_legend=-1)
    # line_chart.title = title
    line_chart.x_labels = [i for i in range(2008, 2018+1)]

    # line_chart.add('C++', [5.6887, 4.8991, 4.9154, 4.2472, 4.0438, 4.1836, 4.0011, 3.7639, 3.3635, 2.978, 2.6638])
    # line_chart.add('Java', [7.5541, 7.1827, 8.0132, 8.5034, 9.0934, 9.5159, 10.2776, 9.9636, 9.1244, 8.4217, 7.796])
    # line_chart.add('Python', [3.6245, 3.8517, 3.9777, 3.5995, 4.0657, 4.9698, 5.7427, 6.6764, 7.8441, 9.9539, 11.5129])

    # line_chart.add('Angular', [0.0017, 0.0015, 0.0004, 0.0012, 0.093, 0.8851, 2.1825, 3.1821, 4.2655, 4.4493, 4.0469])
    # line_chart.add('React', [None, None, None, None, None, 0.0023, 0.0475, 0.323, 0.9032, 1.6016, 2.2517])
    # line_chart.add('Vue.js', [None, None, None, None, None, None, 0.0008, 0.0172, 0.1183, 0.399, 0.652])
    # line_chart.add('jQuery', [1.6408 ,4.3009 ,5.85 ,6.9873 ,7.3793 ,7.4884 ,6.8927 ,5.9547 ,5.1419 ,4.3744 ,3.0976])

    line_chart.add('Wordpress', [0.0977, 0.2284, 0.4884, 0.4943, 0.6767, 0.793, 0.9394, 0.9198, 0.9247, 1.0487, 1.0827])
    line_chart.add('Drupal', [0.0892, 0.2435, 0.4641, 0.3583, 0.2281, 0.1573, 0.1245, 0.1031, 0.0848, 0.0769, 0.0872])
    line_chart.add('Joomla', [0.0326, 0.0861, 0.1232, 0.1304, 0.1817, 0.1962, 0.1452, 0.0797, 0.0624, 0.0468, 0.0364])

    # line_chart.add('Visual Studio Code', [None, None, None, None, None, None, None, 0.0325, 0.0779, 0.1726, 0.2735])
    # line_chart.add('Atom', [None, None, None, None, None, 0.0001, 0.006, 0.0179, 0.0331, 0.0325, 0.0334])
    # line_chart.add('Notepad++', [0.0257, 0.0209, 0.0228, 0.0272, 0.0273, 0.0369, 0.0401, 0.0367, 0.0355, 0.0342, 0.0277])
    # line_chart.add('Sublime Text', [None, 0.0003, 0.0004, 0.0042, 0.0504, 0.0838, 0.0862, 0.0694, 0.0637, 0.0506, 0.0431])
    # line_chart.add('VIM', [0.2983, 0.297, 0.239, 0.2329, 0.2074, 0.1839, 0.1698, 0.1391, 0.1105, 0.0955, 0.0835])

    # line_chart.add('Raspberry Pi', [None, None, None, 0.0002, 0.0089, 0.0488, 0.0683, 0.1032, 0.1232, 0.1469, 0.1649])
    # line_chart.add('Arduino', [0.0137, 0.0145, 0.0133, 0.0225, 0.0496, 0.0753, 0.089, 0.0988, 0.118, 0.1105, 0.1058])

    # line_chart.add('NGINX', [0.0291, 0.0349, 0.0601, 0.0787, 0.115, 0.1437, 0.1878, 0.2207, 0.2564, 0.2989, 0.3214])
    # line_chart.add('Apache', [0.739, 0.6438, 0.6502, 0.6459, 0.7122, 0.7728, 0.9252, 1.1733, 1.4358, 1.5501, 1.6617])
    # line_chart.add('IIS', [1.0407, 0.7023, 0.5071, 0.4408, 0.3531, 0.299, 0.2423, 0.2289, 0.2058, 0.2011, 0.2089])

    # line_chart.add('Eclipse', [0.9413, 0.789, 0.9115, 1.0114, 1.1009, 0.9966, 1.0991, 0.7613, 0.5591, 0.4673, 0.3772])
    # line_chart.add('Android Studio', [None, None, None, 0.0003, 0.0002, 0.0891, 0.1988, 0.4765, 0.6658, 0.4769, 0.6002])

    line_chart.render_to_file(output)

# visualize("Android IDE", "./visualize/output/android_application.svg")
# visualize("JavaScript Framework/Library", "./visualize/output/js_framework.svg")
# visualize("Object-Oriented Language", "./visualize/output/ool.svg")
visualize("CMS", "./visualize/output/cms.svg")
# visualize("Text Editor", "./visualize/output/text_editor.svg")
# visualize("Microcontroller", "./visualize/output/microcontroller.svg")
# visualize("Web Server", "./visualize/output/webserver.svg")

# Below this line is for debugging purpose only
# visualizeSingle("Python", "./dataset/data/tag_counts/topic_based_percentage/TAGS_PYTHON_P.csv",
# "./visualize/output/topic_popularity/python.svg", "PNG")
