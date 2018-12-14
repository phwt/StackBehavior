""" StackBehavior - User Registeration
Convert user registered in a month into consecutive number
"""
import csv

source = "./dataset/data/user_registeration.csv"
output_file = "./dataset/data/user_registeration_converted.csv"

def read(path):
    """ Read raw user registeration file
        Arguments:
            `path` - Input file's path (string)
        Return: List of items in `path` file
    """
    with open(path, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV, None) #Skip header
        data_out = [list(map(int, i)) for i in readCSV]
    return data_out

def convert(data):
    """ Sum data in consecutive sequence
        Arguments:
            `data` - Input data (list)
        Return: List of converted `data`
    """
    last_item = 0
    data_out = list()
    for i in data:
        i[2] += last_item
        data_out.append(i)
        last_item = i[2]
    return data_out

def write(data, output):
    """ Write converted data into specific file
        Arguments:
            `data` - Input data (list)
            `output` - Output file's path (string)
        Return: None
        Output: Converted Comma-Separated Values (.csv) file
    """
    with open(output, 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile)
        [writer.writerow(i) for i in data]
    csvfile.close()

write(convert(read(source)), output_file)
