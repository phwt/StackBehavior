""" StackBehavior - Comments Context
Convert comments context into percentage
"""

import csv

def read(path='./dataset/data/comments_context.csv'):
    """ Read CSV file containing comments data
        Arguments:
            `path` - Input file's path (string)
        Return:
            A list of items in file
    """
    with open(path, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV, None) #Skip header
        data_out = [tuple(map(int, i)) for i in readCSV]
    return data_out

def convert(data):
    data_out = list()
    for i in data:
        pos = (i[1]/sum((i[1], i[2])))*100
        neg = (i[2]/sum((i[1], i[2])))*100
        data_out.append([i[0], round(pos), round(neg), i[3]])
    return zip(*map(lambda i: i[1:3],data_out))

print(*[list(i) for i in convert(read())], sep="\n")