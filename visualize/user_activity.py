""" StackBehavior - User Activity
Visualize user activity in each month into graph
"""
import pygal
import csv

def visualize(output):
    """ Visualize the given data into line graph and render to file
        Arguements:
            `output` - Output file's path (string)
        Return: None
        Output: Vector Graphic (.svg) file
    """
    line_chart = pygal.Line(height=300, show_legend=False, max_scale=8)
    line_chart.title = "User's Activities in each month"
    line_chart.x_labels = [i for i in range(1, 12+1)]
    line_chart.add('', [1333193, 1342918, 1509106, 1440916, 1438207, 1391846, 1455806, 1451272, 1234447, 1301679, 1290436, 1199741])
    line_chart.render_to_file(output)

visualize("./visualize/output/user_activity.svg")