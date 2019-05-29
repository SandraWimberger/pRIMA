#
# Author: Carl Möller
#

"""
Reads a csv file using the panda package
"""

def csv_parser_panda(data):
    import pandas as pd  # Load the Pandas libraries with alias 'pd'
    with open(data, newline='', encoding='utf-8') as file:
    data = pd.read_csv(file)  # Read data from file 'filename.csv'
    return data