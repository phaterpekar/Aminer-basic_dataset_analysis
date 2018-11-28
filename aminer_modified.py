# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:05:41 2018

@author: Ankit
"""
### PROBLEM 1: Aminer : basic dataset analysis
#### A. Compute the number of distinct authors, publication venues, publications, and citations/references
import numpy as np
import pandas as pd

#venues = []
#publications = []
#citations = []
#index = []
#authors = []
#citations = set()
#index=""

dict = {'index':[],'venues':[],'publications':[]} #'authors':[],

citDict ={'index':[],'citations':[]}
authDict = {'index':[], 'authors':[]}

with open("C:\\Unsupervised\\HW1\AP_First15.txt", 'r+', newline='', encoding="utf8") as file:
    for line in file:
        if line.startswith("#index"):
            ind = line[7:].strip('\n').strip('\r')
            #index.append(ind)
            dict['index'].append(ind)
        #elif line.startswith("#@"):
        #    list = []
        #    for auth in line[3:].split(";"):
        #        list.append(auth.strip())
        #    #authors.append(list)
        #    dict['authors'].append(list)
        elif line.startswith("#@"):
            for auth in line[3:].split(";"):
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

            #citations.add(ind +':' + cit)

# with open("C:\\Unsupervised\\HW1\AP_First15.txt", 'r+', newline='', encoding="utf8") as file:
#     for line in file:
#         if line.startswith("#%"):
#             citations.add(index + line)

mainDF = pd.DataFrame.from_dict(dict)
citDF = pd.DataFrame.from_dict(citDict)
authDF = pd.DataFrame.from_dict(authDict)

joinDF = mainDF.join(citDF.set_index('index'), on='index')
newDF = joinDF.join(authDF.set_index('index'), on = 'index')

# len(index)
# len(authors)
#
# index
# index.remove()
# del index[0]
# dict['index'].append(index)
# dict['authors'].append(authors)
#
# dict.keys()
# dict['authors']
# dict['index']
#
# index[0:5]
# authors[0:5]
#
#
#
# len(dict['authors'].values())
#
#
#



#file = open("C:\\Unsupervised\\HW1\AP_train.txt", 'r+', newline='', encoding="utf8")

#print(file.readline())
#iter(file)
#print(next(file))
#with open("C:\\Unsupervised\\HW1\AP_train.txt", 'r+', newline='', encoding="utf8") as file:
    #print(file.readlines(50))
 #   iter(file)
 #   print(next(file))
#file.close()
