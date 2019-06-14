# Calling micro homology dependent deletions
If the 5' bases of a deletion is identical to the 3' bases outside 
the deleted seqeunce the deletion is micro homology dependent. 

The function "micro_homology.py" checks if a micro homology is present in a deletion by comparing the 5' bases in the deleted sequence to the bases in the reference sequence 3' of the deletion

The main script that calls if a deletion is micro homology dependent exists in two version. 
The "micro_homology.py" script is dependent on the built in python csv parser and that the csv file is converted to a nested list.
The "micro_homology_pd.py" script is dependent on the pandas package and that the csv file is converted to a dataframe. 

Both versions will give a csv as output with a new column with the length of the micro homology.

## To run the code
The functions are run from a main script called "microhomology_main.py" or "microhomology_pd.py", depending on what parser/writer one wants to use. The main script will take a .csv file located in the same directiory as input and create a new .csv file in the same directory as output.

### Note
"microhomology_main.py" and "microhomology_pd.py" will give a csv file with and additional column that details the length of the micro homology. All variants not called as "deletion" or called as a deletion with a length <=1 will have an empty cell.
