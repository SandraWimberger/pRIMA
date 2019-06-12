#
#Author: Carl Möller
#
"""
1. imports and parse a csv file formatted according to RIMA
2. looks for micro homologies and adds a column with the length
3. writes the new columns to a csv file and exports it
"""

from csv_parser_panda import csv_parser_panda

test_data = csv_parser_panda("test_dataset.csv")

print(test_data)
# from micro_homology import micro_homo
#
# micro_homology = micro_homo(test_data, 'test_data_refseq')
#
# print(micro_homology)
#
# from csv_writer import csv_writer
#
# test_data = csv_writer(micro_homology, 'test_data_MH.csv')