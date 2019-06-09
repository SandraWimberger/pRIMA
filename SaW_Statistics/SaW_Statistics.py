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
mapped_reads = int(input("How many reads have been mapped? "))

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

#ask where pdf file should be safed

Output_location = input("Where would you like to save this data? ")

### Generating pie charts for editing efficiency
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
with PdfPages((Output_location) + '\pie_plots.pdf') as export_pdf:
    fig = plt.figure()
    fig, (fig1, fig2, fig3) = plt.subplots(3,1)
    
    fig1.pie([float(wt_reads), float(editing_efficiency)], labels=['wt_reads', 'mutated_reads'], pctdistance=0.5, colors=['darkred', 'r'], startangle=90, radius = 1.3, autopct='%.1f%%')
    fig1.set_title('Percent editing efficiency', fontsize=11, pad = 3)
    fig1.axis('equal')
    
    
    # Calculating number of reads with insertions
    insertions = sum(data[data['Type']== 'Insertion']['Count'])
    percent_insertions = insertions/mutated_reads*100
    fig2.pie([float(100 - percent_insertions), float(percent_insertions)], labels=['Others', 'Insertions'], pctdistance=0.5, colors=['b', 'c'], startangle=90, radius = 1.3, autopct='%.1f%%')
    fig2.set_title('Percent insertions from modified reads', fontsize=11, pad = 3)
    fig2.axis('equal') 
    
    
    # Calculating number of reads with deletions
    deletions = sum(data[data['Type']== 'Deletion']['Count'])
    percent_deletions = deletions/mutated_reads*100
    fig3.pie([float(100 - percent_deletions), float(percent_insertions)], labels=['Others', 'Deletions'], pctdistance=0.5, colors=['g', 'y'], startangle=90, radius = 1.3, autopct='%.1f%%')
    fig3.set_title('Percent deletions from modified reads', fontsize=11, pad = 3)
    fig3.axis('equal') 
    
    fig.tight_layout()
    export_pdf.savefig(fig)
    plt.show()
    plt.close()
    
  
    
   


    
    
    
