#
#Author: Carl Möller
#
"""
Checks if a deletion is has a micro homology and exports a list with the length of the homology
"""


def micro_homo(data, refseq):
    # if refseq.endswith('.fasta'):
    #     from Bio import SeqIO
    #     fasta_sequences = SeqIO.parse(open(refseq), 'fasta')
    #         for fasta in fasta_sequences:
    #             name, sequence = fasta.id, str(fasta.seq)
    #     with open(output_file) as out_file:
    micro_homology = []
    with open(refseq) as ref_seq_READ: #open reference sequence
        ref_seq=ref_seq_READ.read()
        print(ref_seq)
    if all(elem in ['Reference Position', 'Type', 'Length', 'Reference', 'Allele', 'Count'] for elem in data[0]):
        #checks if first row contains all of the expecte headers
        print(data[0])
    else:
        raise ValueError("File does not contain the correct headers")
    for i in range(0,len(data)):
        if data[i][data[0].index('Type')] == "Deletion" or data[i][data[0].index('Type')] == "deletion":
            #make note that the refrence position starts with 1
            count=0 #homology length counter
            for char in data[i][data[0].index('Reference')]:
                n=data[i][data[0].index('Reference')].index(char) #tickr to move along the sequence
                if char == ref_seq[int(data[i][data[0].index('Reference Position')])+int(data[i][data[0].index('Length')])-1+n]:
                    count += 1
                else:
                    break
            micro_homology.append(count)
    return micro_homology

