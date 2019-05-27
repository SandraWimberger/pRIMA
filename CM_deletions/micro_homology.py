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

    with open(refseq) as ref_seq_READ: #open reference sequence
        ref_seq=ref_seq_READ.read()
        print(ref_seq)
    if all(elem in ['Reference Position', 'Type', 'Length', 'Reference', 'Allele', 'Count'] for elem in data[0]):
        #checks if first row contains all of the expecte headers
        print(data[0])
    else:
        raise ValueError("File does not contain the correct headers")
    for i in range(0,len(data)):
        if data[i][1] == "Deletion" or data[i][1] == "deletion":
            print(data[i][3])
            print(ref_seq[int(data[i][0])+int(data[i][2])-1])
            #while ref_seq[int(data[i][0])+int(data[i][2])-1] == ref_seq[]

