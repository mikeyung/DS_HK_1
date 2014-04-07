"""
### GA Data Science Class Final Project
###
### Michael Yung
###
### program_3.py
###
### Python program to calculate Euclidean distance - cloest and farthest
###
### Input - Skill files and a new skill set (from my own profile)
### Output -
###
"""

#!/usr/bin/env python

"""

Tag cloud of the skill keywords (Javascript page)
# http://www.jasondavies.com/wordcloud/#http%3A%2F%2Fwww.michaelyung.com%2Fdatascience%2Fdata%2Foutput_connections_skills.csv

"""

import scipy as sp
import sys
import numpy as np
import pandas as pd

from StringIO import StringIO
from sklearn.feature_extraction.text import CountVectorizer

rootpath = '/Users/michaelyung/DS_HK_1/finals/mikeyung/'
skillpath = rootpath + 'output_connections_skills.csv'
urlpath = rootpath + 'output_public_urls.csv'
#filepath = '/Users/michaelyung/DS_HK_1/finals/mikeyung/test.csv'

print "=== Read in public URLs for future referencing ..."
urlfile = open(urlpath, "r" )
allurls = []

for line in urlfile:
    allurls.append( line.strip() )
urlfile.close()

#print allurls

print "=== Read in skill samples ..."
skillfile = open(skillpath, "r" )
allskills = []

for line in skillfile:
    allskills.append( line.strip() )
skillfile.close()

#print allskills

print "=== Vectorize the skills ..."
vectorizer = CountVectorizer(min_df=1)

#print "=== Vectorizer"
#print vectorizer

X = vectorizer.fit_transform(allskills)

#print "=== feature names"
#print vectorizer.get_feature_names()
#print X.toarray().transpose()

num_samples, num_features = X.shape

print "===  Number of samples : ", num_samples
print "=== Number of features : ", num_features

my_skills = "IT Strategy Information Technology Cloud Computing IT Management Project Management Security IT Audit PKI Databases Internet Technologies"
#print "=== my skills"
#print my_skills

my_skills_vec = vectorizer.transform([my_skills])

#print "=== my_skills_vec"
#print my_skills_vec

print "=== Read in my skills ..."
print "      My skills : ", my_skills
# print "My skill vector : "
# print my_skills_vec
# print my_skills_vec.toarray()

def dist(v1, v2):
	delta = v1 - v2
	return sp.linalg.norm(delta.toarray())

def dist_norm(v1, v2):
	v1_normalized = v1/sp.linalg.norm(v1.toarray())
	v2_normalized = v2/sp.linalg.norm(v2.toarray())
	delta = v1_normalized - v2_normalized
	return sp.linalg.norm(delta.toarray())

print "=== Normalize the vector ..."
print "=== Calculate the Euclidean Distance ..."
best_doc = None
best_dist = sys.maxint
best_i = None
worst_dist = 0
worst_i = None
for i in range(0, num_samples):
	skill = allskills[i]

	if skill == my_skills:
		continue
	skill_vec = X.getrow(i)
	d = dist_norm(skill_vec, my_skills_vec)
	if d < best_dist:
		best_dist = d
		best_i = i
	if d > worst_dist:
		worst_dist = d
		worst_i = i

print "==========="
print "Best skill match is connection # : ", best_i
print "         With Euclidean distance : ", best_dist
print "   Connection's domain knowledge : ", allurls[best_i]
print "  Connection's corresponding URL : ", allskills[best_i]

print "==========="
print "Worst skill match is connection # : ", worst_i
print "          With Euclidean distance : ", worst_dist
print "    Connection's domain knowledge : ", allurls[worst_i]
print "   Connection's corresponding URL : ", allskills[worst_i]

# print X.getrow(best_i).toarray()



