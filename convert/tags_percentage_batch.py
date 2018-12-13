""" StackBehavior - Tags Percentage Batch
Reading tags file then compare it with total questions in each year then convert it to percentage in batch
"""

import tags_percentage
import os

output_folder = './dataset/data/tag_counts/topic_based_percentage'

def readBatch(source_folder='./dataset/data/tag_counts/topic_based_year'):
    """ Read each file(s) in the specific folder
        Arguments:
            `source_folder` - Folder containing source files
                              (string - default `./dataset/data/tag_counts/topic_based_year`)
        Return: None
    """
    for subdir, _, files in os.walk(source_folder):
        for file in files:
            path = os.path.join(subdir, file)
            output_path = output_folder+"/"+file[:-4]+"_P"+".csv"
            tags_percentage.convertSingle(path, output_path)
readBatch()
