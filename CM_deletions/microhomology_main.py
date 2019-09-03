#
#Author: Carl Möller
#
"""
1. imports and parse csv file
2. left aligns deletions
3. looks for micro homologies
4. writes the new columns to a csv file and exports it
"""

from csv_csv.csv_parser import csv_parser

test_data = csv_parser('test_dataset.csv')

from CM_deletions.micro_homology import micro_homo

deletions_count = micro_homo(test_data, "REF_SEQ.txt")

print(deletions_count)

from csv_csv.csv_writer import csv_writer

test_data = csv_writer(deletions_count, 'test_data_MH.csv')
