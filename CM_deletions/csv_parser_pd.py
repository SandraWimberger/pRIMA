#
# Author: Carl Möller May 19
#

"""
Parses a csv file with the pandas package. Generating a dataframe
"""

def csv_parser_pd(data):
    import pandas as pd
    dataframe = pd.read_csv(data)
    return dataframe