# Statistically analysis of the Cas9 targeted-sites
## Running the code will calculate the percentage of editing efficiency from mapped reads and percentage of insertions mutated reads. Graphical representation in Pie-charts. 

The code use the variant table as an input file to calcuate different parametes of a Cas9-targeting experiment. 
A test file is provided in the folder ("test_dataset_statistics.csv"). The table is based on NGS variants plus two additional columns (dublications and microhomologies)
Additionally the user needs to provide a the number of mapped reads which can be extracted from the tsv file. 

# How to run the code
## Input
Pandas library is used for dataframe

1. Table of variant in **.csv** format.

|	Reference Position	|	Type	|	Length	|	Reference	|	Allele	|	Count	|	MicroHomology	|	Duplication	|	Rel. Freq.	|
|	------------------- 	|	----------	|	-------	|	-----------------	|	------	|	-----	|	-------------	|	-----------	|	----------	|
|	133	|	Insertion	|	1	|	-	|	T	|	6594	|		|	Detected	|	35.48213517	|
|	121	|	Deletion	|	12	|	TGGAAGCACGAA	|	-	|	1227	|	3	|		|	6.602453724	|
|	130	|	Deletion	|	9	|	GAATGGTTG	|	-	|	854	|	3	|		|	4.595350839	|
|	121	|	Deletion	|	16	|	TGGAAGCACGAATGGT	|	-	|	820	|	5	|		|	4.412397762	|
|	133	|	Deletion	|	1	|	T	|	-	|	689	|		|		|	3.707490314	|
|	134	|	Deletion	|	1	|	G	|	-	|	687	|		|		|	3.696728368	|
|	132	|	Deletion	|	2	|	AT	|	-	|	624	|	0	|		|	3.357727077	|
|	130	|	Deletion	|	4	|	GAAT	|	-	|	515	|	0	|		|	2.771201033	|
|	134	|	Insertion	|	2	|	-	|	AT	|	498	|		|	Detected	|	2.679724494	|
|	133	|	Deletion	|	4	|	TGGT	|	-	|	421	|	3	|		|	2.265389582	|
|	118	|	Deletion	|	16	|	GCCTGGAAGCACGAAT	|	-	|	375	|	0	|		|	2.01786483	|

Relative frequency is calculated in the code
```
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
    print(row)' 

print (data)
```
2. The user will be asked to proved the number of mapped reads. For testing the code any integer can be provided. 
The stastitically calculation will only be performed if the number of mapped reads exceed the number of mutated reads. 
```
mapped_reads = int(input("How many reads have been mapped? "))

mutated_reads = int(data[['Count']].sum())
print (mutated_reads)


while mutated_reads >= mapped_reads:
    print ('Number of mapped reads is lower than number of mutated reads! Try again.')
    mapped_reads = int(input("How many reads have been mapped? "))
    if mutated_reads <= mapped_reads:
        print('Number of mapped reads is bigger than number of mutated reads')
        break
else:
    print('Number of mapped reads is bigger than number of mutated reads')'
```

##Output
