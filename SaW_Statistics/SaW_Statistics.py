import pandas as pd #Load the Pandas libraries with alias 'pd' 
data = pd.read_csv("test_data_statistics.csv") # Read data from file 'filename.csv' [‎2019-‎05-‎29 09:21]  Taheri-Ghahfarokhi, Amir:  
for i in range(10):
    var_type=data.loc[i,'Type']
    var_len=data.loc[i,'Length']
    var_pos=data.loc[i,'Reference Position']
    allele=data.loc[i,'Allele']
    mh_len=data.loc[i,'MicroHomology']
    duplication=data.loc[i,'Duplication']
    row= var_type + " " + str(var_len) + " " + allele
    print(row) 
 
print (data)
#Type in the number of mapped reads from your tsv file
mapped_reads = 50000

# Calculate number of mutated reads
mutated_reads = data[['Count']].sum()
print (mutated_reads)

# Create a new column in the in data frame, calculating relative frequencies

data['rel_freq'] = 100*data['Count']/mapped_reads
print (data)

# Calculating editing efficiency
editing_efficiency = mutated_reads/mapped_reads*100
wt_reads = (100 - editing_efficiency)
print (editing_efficiency) 
print (wt_reads)

### Generating pie charts for editing efficiency
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
pie_editing_efficiency = plt.pie([float(wt_reads), float(editing_efficiency)], labels=['wt_reads', 'mutated_reads'], colors=['r', 'g'], startangle=90, autopct='%.1f%%')


# Calculating number of reads with insertions
insertions = sum(data[data['Type']== 'Insertion']['Count'])
percent_insertions = insertions/mutated_reads*100
pie_insertions = plt.pie([float(100 - percent_insertions), float(percent_insertions)], labels=['Others', 'Insertions'], colors=['r', 'g'], startangle=90, autopct='%.1f%%')


# Calculating number of reads with deletions
deletions = sum(data[data['Type']== 'Deletion']['Count'])
percent_deletions = deletions/mutated_reads*100
pie_deletions = plt.pie([float(100 - percent_deletions), float(percent_insertions)], labels=['Others', 'Deletions'], colors=['r', 'g'], startangle=90, autopct='%.1f%%')

