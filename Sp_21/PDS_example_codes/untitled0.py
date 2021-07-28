#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:04:44 2021

@author: Jen
"""
### Standard loading of libraries
import pandas

import numpy

### setting my working directory here, because I'm always working out of random folders it seems##
from os import chdir, getcwd
wd=getcwd()
chdir(wd)

import os
os.chdir('/Users/Jen/Desktop')


### loading file###Named it data
data = pandas.read_csv('GRSM_003_20162017_Total_Data.csv', low_memory = False)



###Wanted list of column names 
print(data.columns)


###OK here's the good stuff-- So the logic here is that I wanted a table that 
#had year as the rows and OTU or bacterial type (however we want to define that)
##as the columns with the sequence counts as the values for those columns.

##I'm going to do that using the pivot function, unfortunately when I first tried that with this dataset
##I found that there were duplicate bacterial OTUS within each year (which happens with microbiome data)
##That's fine, but it breaks the pivot function.

## here is just a bit of code which summarizes where there are dupilicate OTUs within year
##Not really necesaary, but I wanted to see why I was getting an error and this confirms it.

dupOTUS = data.pivot_table(index='dnaSampleID', columns= 'completeTaxonomy', values='individualCount', aggfunc=len)

##Anyway, my solution to this duplication issue is to have Python combine (sum) any duplicate counts
##within a year. That's what this line of code does. It creates another dataframe (df2) in which it has aggregated 
## any duplications into a single count value by adding them together


df2 = data.groupby(['dnaSampleID', 'completeTaxonomy', 'domain', 'kingdom', 'phylum', 'class', 'order',
       'family', 'genus', 'specificEpithet', 'scientificName'],as_index=False).agg({'individualCount' : "sum"})

##Now to check that that actually happened. All the values here should be 1

No_dup_OTUS = df2.pivot_table(index='dnaSampleID', columns= 'completeTaxonomy', values='individualCount', aggfunc=len)


##So now that we've done that, we can make the table we want. Here I've made it so that 
##the index (rows) are the dnaSampleID (proxy for year or pre or post burn), 
##the columns are the completeTaxonomy (kind of a proxy for OTUS, but we could use another- your call)
##and the values are the total sequence counts. 

biodiv_data = df2.pivot(index='dnaSampleID', columns= 'completeTaxonomy', values='individualCount')



