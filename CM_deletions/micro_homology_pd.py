#
# Author: Carl Möller
#

"""
Checks if a deletion is because a micro homology and exports a list with true or false
Uses a "dataframe" format created by the pandas package
"""

def micro_homo_pd(dataframe, refseq):
    dataframe = dataframe.assign(MHLength=None) #Creates a new column and assigns it as None
    with open(refseq) as ref_seq_READ: #open reference sequence
        ref_seq=ref_seq_READ.read()
        #print(ref_seq)

    #deletions = dataframe.loc[dataframe.loc[:, 'Type'] == "Deletion", ['Reference Position','Reference', 'DelCount']] #extracts reference position and reference seq for all positions called as deletion
    #print(dataframe.iloc[0, :])
    for idx, ref_pos in enumerate(dataframe.iloc[:, 0]):
        #print(ref_pos)
        #print(type(ref_pos))
        if dataframe.iloc[idx, 1] == "Deletion" and dataframe.iloc[idx, 2] > 1:
            count = 0
            for i, char in enumerate(dataframe.iloc[idx, 3]):
                #print(char)
                #print(deletions.iloc[idx, 1])

                if char == ref_seq[ref_pos+dataframe.iloc[idx, 2]-1+i]:
                    count += 1
                else:
                    break
            dataframe.iloc[idx, 6] = count
        else:
            pass
    return(dataframe)