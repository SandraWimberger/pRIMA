#
# Author: Carl Möller
#


def csv_writer_pd(dataframe, filename):
    export = dataframe.to_csv(filename,index = None, header=True)
    return(export)