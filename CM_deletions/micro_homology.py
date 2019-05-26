#
#Author: Carl Möller
#
"""
Checks if a deletion is because a micro homology and exports a list with true or false
"""


def micro_homo(data, refseq):
    # if refseq.endswith('.fasta'):
    #     from Bio import SeqIO
    #     fasta_sequences = SeqIO.parse(open(refseq), 'fasta')
    #         for fasta in fasta_sequences:
    #             name, sequence = fasta.id, str(fasta.seq)
    #     with open(output_file) as out_file:

    with open(refseq) as ref_seq:
    counter = 0
    for i in range(0,len(data)):
        if data[i][1] == "Deletion" or data[i][1] == "deletion":
            counter += 1
            print(data[i][3])
    return counter
