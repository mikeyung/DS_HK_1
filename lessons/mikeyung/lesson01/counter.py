# Use that python binary to execute this script
#
#!/usr/bin/python

#
# First lesson Python script
#
# Michael Yung
# 2014-01-29
#

# Import required libraries

import sys

# Declare counters and store the textfile in memory

impression = 0.0
row = 0
age = 0
total_age = 0.0
total_click = 0
max_age = 0

# Open the file to read
# User .pop(0) to ignore the first line

lines = sys.stdin.readlines()
lines.pop(0)

# For each line, find the numbers in the list.
# The strip() command just to strip spaces before / after the split string, just in case
#
# I suppose I can use function isinstance to test it's string or int ?
#

for line in lines:
	
	clean_line = line.strip().split(',')

	age = int(clean_line[0])
	total_age = total_age + age
	impression = impression + int(clean_line[2])
	total_click = total_click + int(clean_line[3])
	
	if age > max_age:
   		max_age = age

	row = row + 1

# Print out the figures

print '===================='
print '    Impression Sum : ', impression
print '           Age Sum : ', total_age
print '         Click Sum : ', total_click
print '      Total record : ', row
print '===================='

print '       Average Age : %.2f' % ( total_age / row )
print 'Click Through Rate : %0.4f' % ( total_click / impression )
print '     Oldest Person : ', max_age

# Write also to a textfile

file = open("nytimes_results.txt", "w")

file.write('=====================\n')
file.write('     Impression Sum :' + str(impression) + '\n')
file.write('            Age Sum :' + str(total_age) + '\n')
file.write('          Click Sum :' + str(total_click) + '\n')
file.write('       Total record :' + str(row) + '\n')
file.write('=====================\n')

file.write('        Average Age : %.2f' % ( total_age / row ) + '\n')
file.write(' Click Through Rate : %0.4f' % ( total_click / impression ) + '\n')
file.write('      Oldest Person :' + str(max_age) + '\n')

file.close()
