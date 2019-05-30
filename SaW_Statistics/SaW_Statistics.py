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
mapped_reads = 25000

# Calculate number of mutated reads
mutated_reads = data[['Count']].sum()
print (mutated_reads)

# Create a new column in the in data frame, calculating relative frequencies

data['rel_freq'] = 100*data['Count']/mapped_reads
print (data)

# Calculating editing efficiency
editing_efficiency = mutated_reads/mapped_reads
print (editing_efficiency*100) + str(%) 

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # an empty figure with no axes
fig.suptitle('No axes on this figure')  # Add a title so we know which it is

fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
print (fig)