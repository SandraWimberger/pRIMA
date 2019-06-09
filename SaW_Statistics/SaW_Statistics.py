import pandas as pd #Load the Pandas libraries with alias 'pd' 
data = pd.read_csv('test_data_statistics.csv') # Read data from file 'filename.csv' [‎2019-‎05-‎29 09:21]  Taheri-Ghahfarokhi, Amir:  
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
from matplotlib.backends.backend_pdf import PdfPages
with PdfPages(r'C:\Users\kwcb136\Desktop\Charts.pdf') as export_pdf:
    fig1 = plt.figure('Percent editing eficiency')
    pie_editing_efficiency = plt.pie([float(wt_reads), float(editing_efficiency)], labels=['wt_reads', 'mutated_reads'], colors=['darkred', 'r'], startangle=90, autopct='%.1f%%')
    plt.title('Percent editing efficiency')
    export_pdf.savefig(fig1)
    
    # Calculating number of reads with insertions
    insertions = sum(data[data['Type']== 'Insertion']['Count'])
    percent_insertions = insertions/mutated_reads*100
    fig2 = plt.figure('Percent insertions from modified reads')
    pie_insertions = plt.pie([float(100 - percent_insertions), float(percent_insertions)], labels=['Others', 'Insertions'], colors=['b', 'c'], startangle=90, autopct='%.1f%%')
    plt.title('Percent insertions from modified reads')
    export_pdf.savefig(fig2)
    
    # Calculating number of reads with deletions
    deletions = sum(data[data['Type']== 'Deletion']['Count'])
    percent_deletions = deletions/mutated_reads*100
    fig3 = plt.figure('Percent deletions from modified reads')
    plt.pie([float(100 - percent_deletions), float(percent_insertions)], labels=['Others', 'Deletions'], colors=['g', 'y'], startangle=90, autopct='%.1f%%')
    plt.title('Percent deletions from modified reads')
    export_pdf.savefig(fig3)
    plt.show()
    plt.close()
    
    
   


    
    
    
