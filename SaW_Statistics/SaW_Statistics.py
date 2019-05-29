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