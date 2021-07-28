# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas

import numpy


birdWC = pandas.read_csv('brd_countdata.csv', low_memory = False)

#My variable values are NOT numeric in this case, they are character therefore I did not convert to numeric, BUT if I had to:
    #birdWC["VARIABLE"] = birdWC["VARIABLE"].convert_objects(convert_numeric=True)

print(len(birdWC))
print(len(birdWC.columns))


    
print("Number of Observations per Site")
sitecount = birdWC["siteID"].value_counts(sort=False, dropna = False)
print (sitecount)

print("Percentage of Observations per Site")
siteper = birdWC["siteID"].value_counts(sort=False, normalize= True, dropna = False)
print(siteper)

print("Number Bird Taxons Oberved")
taxoncount = birdWC["taxonID"].value_counts(sort=False, dropna = False)
print (taxoncount)


print("Percentage Bird Taxons Oberved")
taxonper = birdWC["taxonID"].value_counts(sort=False, normalize= True, dropna = False)
print(taxonper)


#Alternatively

sitecount1 = birdWC.groupby("siteID").size()
print(sitecount1)

siteper1 = birdWC.groupby("siteID").size()*100/len(birdWC)
print(siteper1)

siteper.to_csv("ew_data.csv")

#Making a table to submit in Canvas

sitecount = pandas.crosstab(index=birdWC["siteID"],  # Make a crosstab
                              columns="count")      # Name the count column

sitecount

sitecount.to_html()

sitecount.to_html("sitecount.html")