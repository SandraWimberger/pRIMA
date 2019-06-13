# -*- coding: utf-8 -*-

Refseq=input("please enter the reference sequence below:\n")
gRNA=input("please enter the gRNA sequence below:\n")

import pandas
df = pandas.read_csv('RIMA.csv', sep=';')
df['Duplication1']=''
count_row=df.shape[0]
df['Duplication1']=''
Refseq='TGCCTGCATTTTAGTCGTGAGATGGAGAATAAAGAAACTCTCAAAGGGTTGCACAAGATGGATGATCGTCCAGAGGAACGAATGATCAGGGAGAAACTGAAGGCAACCTGTATGCCAGCCTGGAAGCACGAATGGTTGGAAAGGAGAAATAGGCGAGGGCCTGTGGTAAGTGGCTATGGG'
gRNA='AGCCTGGAAGCACGAATGGT'
cut=Refseq.find(gRNA[0:16])+16
print(cut,Refseq[cut])
for i in range(0,count_row):
    if df.loc[i]['Allele']!='-':
        allele=df.loc[i]['Allele']
        position=df.loc[i]['Reference Position']
        len_all=len(allele)
        if allele==Refseq[position-1-len_all:position-1] or allele==Refseq[position-1:position+len_all-1]:
            if df.loc[i]['Type']=='Insertion':    
                df.at[i,'Duplication1']='Duplication'
                print(df.loc[i]['Allele'], df.loc[i]['Duplication'],df.loc[i]['Duplication1'])
            else:
                continue
        else:
            continue
    else:    
        continue
df.to_csv('RIMA_Duplication4.csv')
   

