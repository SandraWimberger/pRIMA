# Visualizing Cas9 induced mutation patterns.
Deep sequencing of CRISPR targeted loci provides a robust assay to measure and quantify the Cas9 cutting efficiency and study the induced mutation patterns. This code visualizes a variant table resulted from mutations detected in deep sequencing data.

## Inputs:
1. Table of variant in **.csv** format.
2. Sequence of the **RefSeq**, which has been used to map the reads.
3. Sequence of the **sgRNA**, without PAM.

### Optional inputs:
* Number of variants to visualize. This is by default is 10 variant.
`num_visualized_var = 10`
* Show/hide the drawing window on the screen.
`show_window = True`

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

Linkedin: https://Linkedin.com/Ghahfarokhi
