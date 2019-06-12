#
# Author: Carl Möller
#

"""
Checks if a deletion is because a micro homology and exports a list with true or false
Uses a "dataframe" format created by the pandas package
"""

def micro_homo_pd(dataframe, refseq):
    with open(refseq) as ref_seq_READ: #open reference sequence
        ref_seq=ref_seq_READ.read()
        print(ref_seq)

    deletions = dataframe.loc[dataframe.loc[:, 'Type'] == "Deletion", ['Reference Position','Reference']] #extracts reference position and reference seq for all positions called as deletion
    print(deletions)
    for idx, ref_pos in enumerate(deletions.loc[:,"Reference Position"]):
        #print(idx, ref_pos)
        for char in deletions.iloc[idx, 1]:
            count = 0
            if char == ref_seq[ref_pos+len(deletions.iloc[idx, 1])-1]:
                count +=1
            else:
                break
        dataframe.
         #   if char == ref_seq
