""" StackBehavior - User Registeration Compare Batch
Compare user registeration with asked question for percentage in batch
"""
import user_registeration_compare
import os

output_folder = './dataset/data/question_count/percentage'

def readBatch(source_folder='./dataset/data/question_count/raw'):
    """ Read each file(s) in the specific folder
        Arguments:
            `source_folder` - Folder containing source files
                              (string - default `./dataset/data/question_count/raw`)
        Return: None
        Output: Batch of Converted Comma-Separated Values (.csv) files
    """
    for subdir, _, files in os.walk(source_folder):
        for file in files:
            path = os.path.join(subdir, file)
            output_path = output_folder+"/"+file[:-4]+"_C"+".csv"
            user_registeration_compare.compareSingle(path, output_path)
readBatch()