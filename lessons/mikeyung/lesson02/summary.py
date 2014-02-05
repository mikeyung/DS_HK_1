#!/usr/bin/python

"""

Second lesson Python script - to output a CSV

Michael Yung
2014-01-31
2014-02-05 Add Sorting to the matrix

"""

# Import required libraries

import sys

# Open the file to read
# User .pop(0) to ignore the first line

lines = sys.stdin.readlines()
lines.pop(0)

"""
Initialize variables
"""

age = 0
gender = 0
impression = 0
click = 0
signed_in = 0

"""

For each line, find the numbers in the list.
The strip() command just to strip spaces before / after the split string, just in case

To store the temporary values, need to create a matrix with 10 fields:

age, gender, signed_in
count
total_click, total_impression, max_click, max_impressions

Create a dummy row in the matrix with age 0

"""

summary = [[0, 0, 0, 0, 0, 0, 0, 0]]

for line in lines:
	
	clean_line = line.strip().split(',')

	age = int(clean_line[0])
	gender = int(clean_line[1])
	impression = int(clean_line[2])
	click = int(clean_line[3])
	signed_in = int(clean_line[4])

	match = 1
	for i in range(len(summary)):
		if summary[i][0] == age and summary[i][1] == gender and summary[i][2] == signed_in:
			match = 0
			summary[i][3] += 1
			summary[i][4] += click
			summary[i][5] += impression
			if click > summary[i][6]:
				summary[i][6] = click
			if impression > summary[i][7]:
				summary[i][7] = impression

	if match == 1:
		summary.append([age, gender, signed_in, 1, click, impression, click, impression])

# Sort the matrix, looks like it will ignore the header nicely (or sort it)

summary.sort()

# print summary

# Write also to a SCV

file = open("summary.csv", "w")

file.write('"age", "gender", "signed_in", "avg_click", "avg_impressions", "max_click", "max_impressions"\n')
for i in range(len(summary)):
	age = summary[i][0]
	gender = summary[i][1]
	signed_in = summary[i][2]
	avg_click = float(summary[i][4])/summary[i][3]
	avg_impression = float(summary[i][5])/summary[i][3]
	max_click = summary[i][6]
	max_impressions = summary[i][7]

	file.write(str(age) + ", ")
	file.write(str(gender) + ", ")
	file.write(str(signed_in) + ", ")
	file.write("%.3f" % avg_click + ", ")
	file.write("%.3f" % avg_impression + ", ")
	file.write(str(max_click) + ", ")
	file.write(str(max_impressions))
	file.write("\n")

file.close()
