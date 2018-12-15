import pygal
from pygal.style import Style
style = Style(font_family='googlefont:Athiti', color=('#ff7f50',))
line_chart = pygal.StackedLine(fill=True, range=(60, 100), height=327, max_scale=7, style=style,
    y_title='% จากความคิดเห็นทั้งหมด', legend_at_bottom=True, legend_at_bottom_columns=2)
# line_chart.title = "Comment's context"
line_chart.x_labels = map(str, range(2008, 2018+1))
line_chart.add('ความคิดเห็นเชิงบวก', [88, 87, 85, 84, 84, 82, 80, 78, 78, 78, 77])
line_chart.add('ความคิดเห็นเชิงลบ',  [12, 13, 15, 16, 16, 18, 20, 22, 22, 22, 23])
# line_chart.render_to_file("./visualize/output/comments_context.svg")
line_chart.render_to_file("./visualize/output/comments_context_scaled.svg")