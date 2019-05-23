CLASSIFICATION - DELETION
Takes a deletion larger then 2bp and left aligns it
The function will take a table with called deletions and left align the variants.

1. Load csv formatted table
2. Loop through table -> if marked as deletion

    2a. Check if rightmost nucleotide is the same, if so -> remove it
    2b. Check if the leftmost nucleotide is the same, if so -> remove it

3. Export table with new column with left aligned deletions
This will leave the variant parsimonious(smallest possible representation) and left aligned.

Source:

"   A variant is left aligned if and only if it is no longer possible to shift its position
   to the left while keeping the length of all its alleles constant. "

   https://genome.sph.umich.edu/wiki/Variant_Normalization 20190523