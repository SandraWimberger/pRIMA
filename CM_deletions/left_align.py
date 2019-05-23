#
#Author: Carl Möller
#
"""
Takes a deletion larger then 2bp and left aligns it

"""

def left_align(data):
    for i in range(0,len(data)):
        if data[i][1] == "deletion":

