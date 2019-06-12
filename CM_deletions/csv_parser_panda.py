#
# Author: Carl Möller
#

"""
Reads a csv file using the panda package
"""



def csv_parser_panda(data):
    import pandas as pd  # Load the Pandas libraries with alias 'pd'
    dataframe = pd.read_csv(data, sep=";")  # Read data from file 'filename.csv'

    return dataframe