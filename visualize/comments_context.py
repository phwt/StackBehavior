import pygal
line_chart = pygal.StackedLine(fill=True, range=(0, 100), height=300, max_scale=7)
line_chart.title = "Comment's context"
line_chart.x_labels = map(str, range(2008, 2018+1))
line_chart.add('Positive', [88, 87, 85, 84, 84, 82, 80, 78, 78, 78, 77])
line_chart.add('Negative',  [12, 13, 15, 16, 16, 18, 20, 22, 22, 22, 23])
line_chart.render_to_file("./visualize/output/comments_context.svg")
