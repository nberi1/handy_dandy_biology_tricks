#How to run the checkInserts.py program
##	You need python3 to run this program
#        if you don't have it I can help you install it
#        can install with conda
#
# Open excel and make a table with three columns
# do not use headers (column1 column2 column3 are there as placeholders)
##
#column 1        column2 column3
#>name_of_seq1   FWD_SEQ REV_SEQ
#>name_of_seq2   FWD_SEQ REV_SEQ
#>name_of_seq3   FWD_SEQ REV_SEQ
#
##
#- Name the file guide_oligos
#- Select the ".csv" file type (Commma Separated Text)
#- Save the file to the same folder as your sequencing results
#- Copy checkInserts.py to the same folder
#
#
#- Run the following line of code:
#for FILE in *.seq; do \ python3 checkInserts.py $FILE >> results.txt \ done

import simple_colors
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

#print(args.filename)

# open your file with the sequenced plasmid and
# read it into a string
target_seq = ""

# open the file you want to sequence
with open(args.filename) as querent:
	querent = list(querent)
	target_id = querent[0]
	for field in querent[1:]:
		target_seq += field.rstrip()

# separate a csv line into its component parts
with open('guide_oligos.csv') as oligos:
	for entry in oligos:
		attributes = entry.split(',')
		if target_seq.find(attributes[1]) > 0:
			print('Search string', attributes[0], 'found in', target_id) 
			print(target_seq.replace(attributes[1], simple_colors.green(attributes[1])), "\n\n")

# Include the lines below if you want to also see which sequences were not found
#		else:
#			print('Search string', attributes[0], attributes[1], 'not found in file', target_id)
