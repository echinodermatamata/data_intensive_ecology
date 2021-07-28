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


### Now to use it in skbio you can't have NaN data, so we'll need to replace it with  zeros
##That's what these two lines of code are
biodiv_data0 = biodiv_data.apply (pandas.to_numeric, errors='coerce')
biodiv_data0= biodiv_data.replace(numpy.nan,0)


## Quick check to see that they are all zeros
print (biodiv_data0)



###Now, we've got to get the data into the right type to put into skbio and do all the 
##fun calculations-- specifically we're going to need an array and ids for 
## the library to run on

                               
array = biodiv_data0.to_numpy() 

ids= list(biodiv_data0.index)

### Now that those two objects exist we can plug them in and start getting our 
## analyses back


#### Number of species per site 
from skbio.diversity import alpha_diversity
adiv_obs_otus = alpha_diversity('observed_otus', array, ids)
adiv_obs_otus

## Shannon's for each site
from skbio.diversity import alpha_diversity
shannon= alpha_diversity('shannon', array, ids)


from skbio.diversity import beta_diversity
bc_dm = beta_diversity("braycurtis", array, ids)
print(bc_dm)

from skbio.diversity import block_beta_diversity
uni_dm = block_beta_diversity("unifrac", array, ids)
print(uni_dm)


import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)



### I simplified the .csv file here to make it clear which comparisons we're actually interested in and are biologically relevant
### Feel free to change as needed
data = pandas.read_csv('GRSM Soil Microbe Diversity and Comparison - Bray-Curtis.csv', low_memory = False)
print(data.columns)

##box and whisker plot bc
##This is now the simplified graphs-- I changed the order too. Let me know what you think....
sns.catplot(x="Comp", y="Bray_curtis", hue="Comp", kind="box", data=data, order=[ "Burn/Burn", "Non/Burn", "Burn/Non", "Non/Non"])

#I don't think this is what you're thinking scatterplot
chart = sns.catplot(x="Comp", y="Bray_curtis", data=data, order=[ "Burn/Burn", "Non/Burn", "Burn/Non", "Non/Non"])
chart.set_xticklabels(rotation = 45)

##violin plot in hopes that it makes a less ugly graph
sns.catplot(x="Bray_curtis", y="Comp", hue="Comp", kind="violin", data=data, order=[ "Burn/Burn", "Non/Burn", "Burn/Non", "Non/Non"])                       


### OK time for stats
import scipy.stats as stats

stats.f_oneway(data["Bray_curtis"][data['Comp'] == 'Burn/Burn'],
               data['Bray_curtis'][data['Comp'] == 'Non/Burn'],
               data['Bray_curtis'][data['Comp'] == 'Burn/Non'],
              data['Bray_curtis'][data['Comp'] == 'Non/Non'])


### OK time for stats
import scipy.stats as stats

stats.f_oneway(data["DO"][data['siteID'] == 'BART'],
               data['DO'][data['siteID'] == 'FLINT],
              data['DO'][data['siteID'] == 'MAYF'])

### this is an ANOVA comparing the 4 different groups we made 
## You can see by the output table that overall, there isn't a significant difference between groups, but
## where we really expect there to be a difference there might be, so we do an additional test

from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(endog=data['Bray_curtis'], groups=data['Comp'], alpha=0.05)
print(tukey)

### Here what you're seeing is a tukey test between groups within an ANOVA
### In the results table what you see is that there is a significant difference between Burn/ Burn and Non/Non 
### Which is what we expect!!! Yeah!!!


stats.ttest_ind(data["Bray_curtis"][data['Comp2'] == 'Burn/Burn'],
                data['Bray_curtis'][data['Comp2'] == 'Non/Non'])



###### TAKING THE TOP 50 GENERA TO MAKE STACKED BAR GRAPHS
## use the df2 dataframe

df20 = df2.apply (pandas.to_numeric, errors='coerce')
df20= df20.replace(numpy.nan,0)

df20['dnaSampleID'] = df20['dnaSampleID'].astype(str)

mystr = df20['dnaSampleID']
mystr[18:25]

df20['dnaSampleID'].str.contains('20160720')18:25