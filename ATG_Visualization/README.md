# Visualizing Cas9 induced mutation patterns.
Deep sequencing of CRISPR targeted loci provides a robust assay to measure and quantify the Cas9 cutting efficiency and study the induced mutation patterns. This code visualizes a variant table resulted from mutations detected in deep sequencing data.

## Inputs:
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

2. Sequence of the **RefSeq**, which has been used to map the reads.
`refseq="TGCCTGCATTTTAGTCGTGAGATGGAGAATAAAGAAACTCTCAAAGGGTTGCACAAGATGGATGATCGTCCAGAGGAACGAATGATCAGGGAGAAACTGAAGGCAACCTGTATGCCAGCCTGGAAGCACGAATGGTTGGAAAGGAGAAATAGGCGAGGGCCTGTGGTAAGTGGCTATGGG"`
3. Sequence of the **sgRNA**, without PAM.
`sgrna="AGCCTGGAAGCACGAATGGT"`

### Optional inputs:
* Number of variants to visualize. This is by default is 10 variant.
`num_visualized_var = 10`
* Show/hide the drawing window on the screen.
`show_window = True`
* Colors for the different type of mutations:
```
shape_fill={"match":"light gray",
            "match_border":"light gray",
            "deletion":"black",
            "deletion_border":"black",
            "insertion":"red",
            "insertion_border":"black",
            "duplication":"yellow",
            "duplication_border":"black",
            "microhomology":"cyan",
            "microhomology_border":"black",
            "sgrna_border":"gray",
            "sgrna":"pink",
            "sgrna_text":"black",
            "pam":"yellow",
            "pam_border":"orange",
            "cut_line":"green"
            }
```

## Requirements:
This code uses the following packages:
 ```
 turtle
 tkinter
 pandas
 ```


## Output:
The resulting visualized variants will be saved as _**.eps**_ format in the same directory. 

![Output screenshot](https://github.com/SandraWimberger/pRIMA/blob/master/ATG_Visualization/Output_Screen_Capture.JPG)

### Author: 
Amir Taheri-Ghahfarokhi

Email: Amir.Taheri-Ghahfarokhi@astrazeneca.com

[Link to Linkedin!](https://www.linkedin.com/in/ghahfarokhi/)
