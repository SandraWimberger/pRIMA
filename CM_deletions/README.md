#Calling micro homology dependent deletions
If the initial bases of a deletion is identical to the bases immidiately after 
the deleted seqeunce the deletion is micro homology dependent. 

The function checks if a micro homology is present in the deletion by comparing the 5' bases in the deletion
to the bases present immediatly after the deletion

Take a left aligned deletion and loop trough the bases starting from the 5' end of the deleted sequence
and compare to the bases in the reference sequence 3' of the deletion.


The main script that calls if a deletion is micro homology dependent exists in two version as of 20190613. 
The "micro_homology.py" uses the built in python csv parser/writer to handle the data.
The "micro_homology_pd.py" uses the pandas package to convert the csv to a dataframe. 
This is in line with the data format used in the rest of this project.

Both versions will give a csv as output with a new column with the length of the micro homology.
##Input
"deletions_main" will take a .csv file located in the same directiory as input.
##Output
