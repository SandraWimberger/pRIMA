#
#Author: Carl Möller
#
"""
Checks if a deletion is because a micro homology and exports a list with true or false
"""


def micro_homo(data):
    counter = 0
    for i in range(0,len(data)):
        if data[i][1] == "Deletion" or data[i][1] == "deletion":
            counter += 1
            print(data[i][3])
    return counter
