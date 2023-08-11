#! /home/nberi/miniconda3/bin/python

# this is a program to do solution dilutions for you since it is a PITA
# annotate numbers with mL, uL, nL etc
# inputs: -c1 -v1 -c2 -v2 (three of four)
# first version will take the first three and get v2

# second version will take user inputs 
# and accept a blank input as the value to compute

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("c1")
parser.add_argument("c1_units")
parser.add_argument("v1")
parser.add_argument("v1_units")
parser.add_argument("c2")
parser.add_argument("c2_units")
args = parser.parse_args()
print(args.c1)

conc1 = int(args.c1)
conc1_units = args.c1_units
vol1 = int(args.v1)
vol1_units = args.v1_units
conc2 = int(args.c2)
conc2_units = args.c2_units

# Print all four numbers with their appropriate units
print(\
 "Conc 1:\t", str(conc1), conc1_units,\
 "\n Vol 1:\t", vol1, vol1_units,\
 "\nConc 2:\t", conc2, conc2_units )#,\
# "\n Vol 2:\t", vol2, vol2_units, "\n"\
# )

# make serial dilution dict
unit_list = ["L", "mL", "uL", "nL", "pL"]
#print(unit_list[0])

# make function to convert units
def convert_units(val, units, ul):
	original_val = val
	original_index = ul.index(units)
	i = original_index
	if val <= 1000 and val >= 1:
		val2 = val
#		print("Units can stay the same", val2, units)
	elif val >= 1000:
		valence = "higher"
#		print("Need to change units")
		while val >= 1000:
			val = val / 1000
			i = i - 1
		val2 = int(val)
	final_index = original_index - i
	final_units = ul[final_index]
#	val2 = int(val2)
#	print("The final figure is", val2, final_units, "which is equivalent to", original_val, units)
	return(val2, final_units)

# make function to do the math
# ("seeone") like C1
def seeone(c1, v1, c2):
	v2 = int(c1 * v1 / c2)
#	print(" Vol 2:", v2)
	return(v2)

vol2 = seeone(conc1, vol1, conc2)

#print(" Vol 2:", vol2)
# do the unit conversion
number, units = convert_units(vol2, "uL", unit_list)

print(" Vol 2:\t", number, units)
