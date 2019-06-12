#type in reference sequence
#type in gRNA sequence

#import file"RIMA.csv"
#import pandas library
#create a new columne named"Duplication1"
#check values in columne "Allele" from the first row to the last row by order
    if it's not "-", if the value in columne "Type" in the same row is "Insertion", do the following steps:
        check if the value in columne "Allele" is a direct repeat sequence or nucleotide to the sequence left to it or right to it.
            if yes, add value "Duplication" in columne "Duplication1", otherwise skip
    if the value in columne "Allele" is "-", then skip it.

#Export the modified data as new csv file "RIMA_Duplication.csv"
    
    
