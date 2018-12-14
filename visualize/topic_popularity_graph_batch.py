""" StackBehavior - Topic Popularity Graph Batch
Visualize topic popularity data in batch into line graph format.
"""
import pygal
import csv
import topic_popularity_graph
import os

output_folder = './visualize/output/topics'

def readBatch(source_folder='./dataset/data/tag_counts/topic_based_percentage'):
    """ Read each file(s) in the specific folder
        Arguments:
            `source_folder` - Folder containing source files
                              (string - default `./dataset/data/tag_counts/topic_based_percentage`)
        Return: None
        Output: Batch of Converted Comma-Separated Values (.csv) files
    """
    for subdir, _, files in os.walk(source_folder):
        for file in files:
            path = os.path.join(subdir, file)
            output_path = output_folder+"/"+file[:-4]+"_P"+".csv"
            tags_percentage.convertSingle(path, output_path)
readBatch()