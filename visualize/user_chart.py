""" StackBehavior - User Chart
This module visualize user count by country into bar chart using pygal library
"""
import pygal
import csv

def read():
    """ Convert data from an csv file into dict """
    data_dict, country_dict, cur_row = {}, {}, 0
    with open('./dataset/data/pygal_supported_country.csv', encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            country_dict[row[0]] = row[1]
            if cur_row == 183:
                break
            cur_row += 1

    with open('./dataset/data/user_location_min.csv', encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            data_dict[country_dict[row[0]]] = int(row[1])
    return dict(sorted(data_dict.items(), key=lambda i: i[1], reverse=True)[0:11])

def visualize():
    data_dict = read()
    line_chart = pygal.Bar(show_legend=False)
    line_chart.title = 'Top 10 countries with most user of StackOverflow'
    line_chart.x_labels = [i for i in data_dict]
    line_chart.add("Total", [i[1] for i in data_dict.items()])
    line_chart.render_to_file('./visualize/output/user_chart.svg')
visualize()
