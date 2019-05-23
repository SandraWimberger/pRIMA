CLASSIFICATION - DELETION
Checks if a micro homology is present in the deletion by comparing the 5' bases in the deletion
to the bases present immediatly after the deletion

Take a left aligned deletion and loop trough the bases starting from the 5' end of the deletion
and compare to the bases 3' of the deletion.

while del.seq == 3' seq there is a homology
