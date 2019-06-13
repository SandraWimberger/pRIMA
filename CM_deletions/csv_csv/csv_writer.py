#
#Author: Carl Möller May -19
#
"""
Takes a list of lists and writes it to a csv file.
The function assumes that the first list contains headers
The functions accepts two arguments, first one is the data to be written to csv and the second one the filename for the
csv file. Make sure to add the .csv exstension to the filename.
File will be saved to the same folder as the script is run from.
"""
import csv
def csv_writer(data, file_name):
    myFile = open(file_name, 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(data)

    return myFile