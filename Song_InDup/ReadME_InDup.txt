Creating a new columne named "Duplication"
Checking the sequence in columne "Allele"
if it's "-", add "" in columne "Duplication"
if it's a sequence, matching it to the sequence left to it
    if match, add "Detected" in columne "Duplication"
    if not match, match it to the seqeuence right to it
    if match, add "Detected" in columne "Duplication"
    if not match, add "" in columne "Duplication"