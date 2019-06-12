#
#Author: Carl Möller
#
"""
Checks if a deletion is because a micro homology and exports a list with true or false
"""


def micro_homo(data, refseq):
    #checks if the ingoing reference sequence is a fasta file and parses it
    if refseq.endswith('.fasta'):
        from Bio import SeqIO
        ref_seq = SeqIO.parse(open(refseq), 'fasta')
        for fasta in ref_seq:
            name, sequence = fasta.id, str(fasta.seq)
    else:
        pass

    with open(refseq) as ref_seq_READ: #open reference sequence
        ref_seq=ref_seq_READ.read()
        print(ref_seq)
    if all(elem in ['Reference Position', 'Type', 'Length', 'Reference', 'Allele', 'Count'] for elem in data[0]):
        #checks if first row contains all of the expected headers
        print(data[0])
    else:
        raise ValueError("File does not contain the correct headers")

    for i in range(1,len(data)): #expects first list to be headers
        if data[i][data[0].index('Type')] == "Deletion":
            #make note that the refrence position starts with 1
            count=0 #homology length counter
            for char in data[i][data[0].index('Reference')]:
                n=data[i][data[0].index('Reference')].index(char) #tickr to move along the sequence
                if char == ref_seq[int(data[i][data[0].index('Reference Position')])+int(data[i][data[0].index('Length')])-1+n]:
                    count += 1
                else:
                    break
        else:
            count = 0 # adds a 0 to "non-deletion" positions
        data[i].extend(str(count)) #adds the deletion length to the list

    return data