""" StackBehavior - Tags Percentage
Reading tags file then compare it with total questions in each year then convert it to percentage
"""

import csv

def readInt(path, header=True):
    """ Read CSV file containing only integer data
        Arguments:
            `path` - Input file's path (string)
            `header` - Skip the header (boolean - default `True`)
        Return:
            A list of every row read from `path` file
            Sample - [(2008, 40), (2009, 2029)...(2018, 99904)]
    """
    with open(path, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV, None) if header else 0 #Skip header if header == True
        data_out = [tuple(map(int, i)) for i in readCSV]
    return data_out

def percentage(data, count):
    """ Compare counts to total number of questions in each year
        Arguments:
            `data` - Data to be compared (list)
            `count` - Question count data (list)
        Return:
            A list of compared data in format of (year, percentage) in four decimal
            Sample - [(2008, 0.0686), (2009, 0.5903)...(2018, 6.4591)]
    """
    count = dict(count)
    return [(i, round((j/count.get(i))*100, 4)) for i, j in data]

def writeFile(data, output):
    """ Write calculated percentage with tags name to the output file
        Arguments:
            `data` - Data to be written (list)
            `output` - Output file's path (string)
    """
    with open(output, 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile)
        [writer.writerow(i) for i in data]
    csvfile.close()

def convertSingle(source, output):
    """ Read single file, convert to percentage then write to output file
        Arguments:
            `source` - Source file's path (string)
            `output` - Output(Result) file's path (string)
        Return: None
    """
    question_count = readInt('./dataset/data/question_count_by_year.csv')
    tags_count = readInt(source)
    converted = percentage(tags_count, question_count)
    writeFile(converted, output)

# Below this line is for debugging purpose only
# convertSingle('./dataset/data/tag_counts/topic_based_year/TAGS_ANDROID.csv', \
# './dataset/data/tag_counts/tags_count_test.csv')
