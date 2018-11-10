""" User World Map
This module visualize user count by country in to world map using pygal library
"""
import pygal
import csv
from pygal.style import Style

custom_style = Style(
  colors=('#F6D18B', '#F0AE58', '#EF8823', '#EB7A3E', '#F05328'))

def read(stt, stp=0):
    """ Convert data from an csv file into dict """
    data_dict = {}
    with open('./dataset/data/user_location_min.csv', encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if stt <= int(row[1]) <= stp or (int(row[1]) >= stt and not stp):
                # data_dict[row[0]] = int(row[1])
                data_dict[row[0]] = 1
    return data_dict

def visualize():
    worldmap_chart = pygal.maps.world.World(style=custom_style)
    worldmap_chart.title = 'StackOverflow users by country'
    worldmap_chart.add('1 - 10000', read(1, 10000))
    worldmap_chart.add('10001 - 40000', read(10001, 40000))
    worldmap_chart.add('40001 - 80000', read(40001, 80000))
    worldmap_chart.add('80001 - 140000', read(80001, 140000))
    worldmap_chart.add('140000+', read(140001))
    worldmap_chart.render_to_file('./visualize/output/user_world_map.svg')
visualize()
