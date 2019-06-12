#
# Author: Carl Möller
#

"""
Checks if a deletion is because a micro homology and exports a list with true or false
Uses a "dataframe" format created by the pandas package
"""

def micro_homo_pd(dataframe, refseq):
    dataframe = dataframe.assign(DelCount=None) #Creates a new column and assigns it as None
    with open(refseq) as ref_seq_READ: #open reference sequence
        ref_seq=ref_seq_READ.read()
        print(ref_seq)

    deletions = dataframe.loc[dataframe.loc[:, 'Type'] == "Deletion", ['Reference Position','Reference', 'DelCount']] #extracts reference position and reference seq for all positions called as deletion
    print(deletions)
    for idx, ref_pos in enumerate(deletions.loc[:,"Reference Position"]):
        #print(ref_pos)
        #print(type(ref_pos))

        if len(deletions.iloc[idx, 1]) <= 1:
            deletions.iloc[idx, 2] = None
        else:
            count = 0
            for i, char in enumerate(deletions.iloc[idx, 1]):
                print(char)
                #print(deletions.iloc[idx, 1])

                if char == ref_seq[ref_pos+len(deletions.iloc[idx, 1])-1+i]:
                    count += 1
                else:
                    break
            print(ref_seq)
            print(deletions.iloc[idx, 1])
            deletions.iloc[idx, 2] = count
             #   if char == ref_seq
    print(deletions)