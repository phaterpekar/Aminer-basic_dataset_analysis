# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:05:41 2018

@author: Ankit
"""
### PROBLEM 1: Aminer : basic dataset analysis
#### A. Compute the number of distinct authors, publication venues, publications, and citations/references
import numpy as np
import pandas as pd

dict = {'index':[],'venues':[],'publications':[]}
citDict ={'index':[],'citations':[]}
authDict = {'index':[], 'authors':[]}

with open("C:\\Unsupervised\\HW1\AP_train.txt", 'r+', newline='', encoding="utf8") as file: #AP_First15.txt AP_train.txt
    for line in file:
        if line.startswith("#index"):
            ind = line[7:].strip('\n').strip('\r')
            dict['index'].append(ind)
        elif line.startswith("#@"):
            for auth in line[3:].split(";"):
                auth = auth.strip('\n').strip('\r')
                authDict['index'].append(ind)
                authDict['authors'].append(auth)
        elif line.startswith("#c"):
            ven = line[2:].strip()
            dict['venues'].append(ven)
        elif line.startswith("#*"):
            pub = line[2:].strip()
            dict['publications'].append(pub)
        elif line.startswith("#%"):
            cit = line[2:].strip()
            citDict['index'].append(ind)
            citDict['citations'].append(cit)

mainDF = pd.DataFrame.from_dict(dict)
citDF = pd.DataFrame.from_dict(citDict)
authDF = pd.DataFrame.from_dict(authDict)


# Total number of Citations :
print(len(citDF.citations))

# Total number of Publications:
print(len(mainDF.publications))

# Total number of Distinct Authors:
authDF = authDF.replace('', np.NaN)
print(authDF.authors.nunique())

# Total number of venues
print(mainDF.venues.nunique())


# B. The Count numbers don't seem accurate. For the same conference, we can see that the venues have different names.
# While a different publication don't have the same names. This will increase our count of venues than the true count as it is not consistent.

mainDF['venues'][mainDF['venues'].str.contains('Principles and Practice of Knowledge Discovery in Databases')].unique()



