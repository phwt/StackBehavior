""" StackBehavior - User Registeration Compare
Compare user registeration with asked question for percentage
"""
import csv
import os

def getUser(year, month):
    """ Read user registeration file and return current user registered in entered time.
        Arguments:
            `year` - Year (int 2008 - 2018)
            `month` - Month (int 1 - 12)
        Return:
            Number of total registered user at `year` and `month`
    """
    path = './dataset/data/user_registeration_converted.csv'
    with open(path, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        return int([i for i in readCSV if i[0] == str(year) and i[1] == str(month)][0][2])

def read(path):
    """ Read user registeration file and return current user registered in entered time.
        Arguments:
            `path` - File's path (string)
        Return:
            List of item in `path` file
    """
    with open(path, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV, None) #Skip header
        year = int(path.split("_")[-1].rstrip(".csv"))
        return year, [tuple(map(int, i)) for i in readCSV]

def convert(data):
    """ Compare questions with user registered at the time and return in 4-decimal places.
        Arguments:
            `data` - Input data (list)
        Return:
            A list of converted data
    """
    data_out = list()
    for i in data[1]:
        data_out.append((i[0], round(i[1]/getUser(data[0], i[0]), 4)))
    return data_out

def writeFile(data, output):
    """ Write calculated percentage with tags name to the output file
        Arguments:
            `data` - Data to be written (list)
            `output` - Output file's path (string)
        Return: None
    """
    with open(output, 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile)
        [writer.writerow(i) for i in data]
    csvfile.close()

def compareSingle(soruce, output):
    """ Comparing single file """
    writeFile(convert(read(soruce)), output)

# Below this line is for debugging purpose only
# compareSingle("./dataset/data/question_count/raw/QUESTION_2008.csv", \
# "./dataset/data/question_count/percentage/QUESTION_2008_C.csv")