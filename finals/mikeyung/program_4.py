"""
### GA Data Science Class Final Project
###
### Michael Yung
###
### program_4.py
###
### Python program to do clustering
###
### Input - Skill files and a new skill set (from my own profile)
### Output -
###
"""

#!/usr/bin/env python

import scipy as sp
import sys
import numpy as np
import pandas as pd

from StringIO import StringIO
from sklearn.feature_extraction.text import CountVectorizer
import sklearn.datasets
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances

rootpath = '/Users/michaelyung/DS_HK_1/finals/mikeyung/'
skillpath = rootpath + 'output_connections_skills.csv'

"""
Read in all the skills
Learn the vocabulary dictionary and return the count vectors
"""

print "=== Reading in skill samples ..."
skillfile = open(skillpath, "r" )
allskills = []

for line in skillfile:
    allskills.append( line.strip() )
skillfile.close()

#print allskills
#raw_input("Press Enter to continue...")

"""
Vectorize the skills
X is array of word label and the count for each connection's skills
"""

print "=== Vectorizing the skills ..."

vectorizer = CountVectorizer(min_df=1)
X = vectorizer.fit_transform(allskills)

print "=== Skill Vector"
# print X
print X.toarray()


raw_input("Press Enter to continue...")

#print "=== feature names"
#print vectorizer.get_feature_names()

#raw_input("Press Enter to continue...")


num_samples, num_features = X.shape

print "=== Skill Vector Shape"
print "===  Number of samples : ", num_samples
print "=== Number of features : ", num_features

"""
Set number of clusters and start KMeans
Form clusters ...
"""

num_clusters = 10
print "=== Grouping to clusters"
print "Number of clusters :", num_clusters


km = KMeans(n_clusters=num_clusters, init='k-means++', n_init=1, verbose=1)
km.fit(X)

raw_input("Press Enter to continue...")


print "=== km.labels_ : "
print km.labels_

print "=== km.labels_.shape : ", km.labels_.shape
centroids = km.cluster_centers_
print "=== centroids : "
print centroids
print centroids.shape

#z = euclidean_distances(centroids, centroids)
#print "=== z"
#print z
#print z.shape


"""
Input my skills to give check what cluster it belongs to

similar_indices is the similar post in the same cluster

"""

my_skills = "IT Strategy Information Technology Cloud Computing IT Management Project Management Security IT Audit PKI Databases Internet Technologies"
my_skills_vec = vectorizer.transform([my_skills])
my_skill_label = km.predict(my_skills_vec)[0]
similar_indices = (km.labels_==my_skill_label).nonzero()[0]

print "=== Read in my skills ..."
print "      My skills : ", my_skills
#print "=== My skill vector : "
#print my_skills_vec
#print "=== My skill vector array : "
#print my_skills_vec.toarray()

zz = euclidean_distances(centroids, my_skills_vec)
print "=== Distance to the 10 centroids"
print zz
print "=== Closet to cluster # :", my_skill_label
print "=== Skill sets in the same cluster :", similar_indices
print "=== No. of skill sets in the same cluster :", similar_indices.shape

"""
Similar skill sets in the same cluster
"""

similar = []
for i in similar_indices:
	dist = sp.linalg.norm((my_skills_vec - X[i]).toarray())
	similar.append((dist, allskills[i]))
similar = sorted(similar)


# print "=== Similar"
# print similar

show_at_1 = similar[0]
show_at_2 = similar[len(similar)/2]
show_at_3 = similar[-1]

print "=== Within the same cluster, the skillsets and distance"
print show_at_1
print show_at_2
print show_at_3


