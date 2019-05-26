#
#Author: Carl Möller
#
"""
1. imports and parse csv file
2. left aligns deletions
3. looks for micro homologies
4. writes the new columns to a csv file and exports it
"""

from csv_parser import csv_parser

test_data = csv_parser('test_dataset.csv')

from micro_homology import micro_homo

deletions_count = micro_homo(test_data)

print(deletions_count)