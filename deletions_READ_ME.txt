CLASSIFICATION - DELETION
Takes a deletion larger then 2bp and left aligns it
The function will take a table with called deletions and left align the variants.

1. Check if rightmost nucleotide is the same, if so -> remove it
2. Check if the leftmost nucleotide is the same, if so -> remove it

This will leave the variant parsimonious(smallest possible representation) and left aligned.
