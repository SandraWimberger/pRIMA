#
# Author: Carl Möller May 19
#

from csv_csv_pandas.csv_parser_pd import csv_parser_pd

test_data = csv_parser_pd("test_dataset.csv")

from micro_homology_pd import micro_homo_pd

data = micro_homo_pd(test_data, "test_data_refseq")


from csv_csv_pandas.csv_writer_pd import csv_writer_pd

test_data = csv_writer_pd(data, 'test_data_MH.csv')