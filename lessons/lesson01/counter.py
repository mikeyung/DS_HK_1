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
#
# I suppose I can use function isinstance to test it's string or int ?
#

for line in lines:
   age = int(line.strip().split(',')[0])
   total_age = total_age + age
   impression = impression + int(line.strip().split(',')[2])
   total_click = total_click + int(line.strip().split(',')[3])
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
print 'Click through rate : %0.4f' % ( total_click / impression )
print '     Oldest person : ', max_age

# Write also to a textfile

file = open("nytimes_results.txt", "w")

file.write('=====================\n')
file.write('     Impression Sum :' + str(impression) + '\n')
file.write('            Age Sum :' + str(total_age) + '\n')
file.write('          Click Sum :' + str(total_click) + '\n')
file.write('       Total record :' + str(row) + '\n')
file.write('=====================\n')

file.write('        Average Age : %.2f' % ( total_age / row ) + '\n')
file.write(' Click through rate : %0.4f' % ( total_click / impression ) + '\n')
file.write('      Oldest person :' + str(max_age) + '\n')

file.close()
