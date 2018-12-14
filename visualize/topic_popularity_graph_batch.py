""" StackBehavior - Topic Popularity Graph Batch
Visualize topic popularity data in batch into line graph format.
"""
import csv
import topic_popularity_graph
import os

output_folder = './visualize/output/topic_popularity'

def readBatch(file_format="SVG", source_folder='./dataset/data/tag_counts/topic_based_percentage'):
    """ Read each file(s) in the specific folder
        Arguments:
            `source_folder` - Folder containing source files
                              (string - default `./dataset/data/tag_counts/topic_based_percentage`)
            `file_format` - Output file's format (`PNG` of `SVG`(default))
        Return: None
        Output: Batch of Converted Comma-Separated Values (.csv) files
    """
    for subdir, _, files in os.walk(source_folder):
        for file in files:
            path = os.path.join(subdir, file)
            topic = file.split("_")[1]
            output_path = output_folder+"/"+topic+"_V"+(".svg" if file_format == "SVG" else ".png")
            topic_popularity_graph.visualizeSingle(topic, path, output_path, file_format)
            # print(topic, path, output_path)
            # break
readBatch("SVG")
