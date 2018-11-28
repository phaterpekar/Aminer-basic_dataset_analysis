# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:05:41 2018

@author: Ankit
"""
### PROBLEM 1: Aminer : basic dataset analysis
#### A. Compute the number of distinct authors, publication venues, publications, and citations/references

authors = set()
venues = set()
publications = set()
citations = set()
index = ""

with open("C:\\Unsupervised\\HW1\AP_train.txt", 'r+', newline='', encoding="utf8") as file:
    for line in file:
        if line.startswith("#index"):
            index = line[7:]
            publications.add(line)
        elif line.startswith("#@"):
            for auth in line[3:].split(";"):
                authors.add(auth.strip())
        elif line.startswith("#c"):
            venues.add(line)
        elif line.startswith("#%"):
            citations.add(index + line)

print("Total number of Distinct Authors", len(authors))
print("Total number of Venues", len(venues))
print("Total number of Publications", len(publications))
print("Total number of Citations/Referenes", len(citations))

#### B. Are these numbers likely to be accurate?
### As an example look up all the publications venue names associated with the conference
### “Principles and Practice of Knowledge Discovery in Databases”13 – what do you notice?

venue_set = set()

with open("C:\\Unsupervised\\HW1\AP_train.txt", 'r', newline='', encoding="utf8") as apfile:
    index = ""
    venue = ""
    for row in apfile:
        if row.startswith("#c"):
            if "Principles and Practice of Knowledge Discovery in Databases" in row:
                venue = row[3:]
                venue_set.add(venue)

print("Venues lists are ")
for venue in venue_set:
    print(venue)

# The Count numbers don't seem accurate.


#### C. For each author, construct the list of publications.
### Plot a histogram of the number of publications per author (use a logarithmic scale on the y axis)

author_publications = {}

# Considering each Citation as one
with open("C:\\Unsupervised\\HW1\AP_train.txt", 'r', newline='', encoding="utf8") as apfile:
    for row in apfile:
        if row.startswith("#@"):
            for column in row[3:].split(";"):
                if author_publications.get(column.strip()) == None:
                    author_publications[column.strip()] = 1
                else:
                    author_publications[column.strip()] += 1

authors = list(author_publications.keys())
publications = list(author_publications.values())

# Removing values for the null author and it's respective publication count ,
# because it is an outlier in this case and has a value much greater than the mean.

null_index = authors.index("")
del authors[null_index]
del publications[null_index]

import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

plt.xlabel('Authors')
plt.ylabel('Publications')
plt.title('Histogram of Publications per author')
plt.grid(True)

plt.hist(publications, bins=50, log=True)
plt.show()
