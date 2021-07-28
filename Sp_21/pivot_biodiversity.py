#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 09:45:21 2021

@author: Jen
"""

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
os.chdir('/Users/Jen/Downloads/')


### loading file###Named it data
data = pandas.read_csv('inv_taxonomyProcessed.csv', low_memory = False)



###Wanted list of column names 
print(data.columns)



###OK here's the good stuff-- So the logic here is that I wanted a table that 
#had year as the rows and species or OTUs as they are called in this package (Operational Taxonomic Unit-- which is whatever level of taxonomy you want)
##as the columns with the sequence counts as the values for those columns.

##I'm going to do that using the pivot function, unfortunately when I first tried that with this dataset
##I found that there were duplicate taxonID counts for each plotID/setDate combo (which happens)
##That's fine, but it breaks the pivot function.

## here is just a bit of code which summarizes where there are dupilicates within year
##Not really necesaary, but I wanted to see why I was getting an error and this confirms it.

dups = data.pivot_table(index=["collectDate",'siteID'], columns= 'scientificName', values='individualCount', aggfunc=len)

##Anyway, my solution to this duplication issue is to have Python combine (sum) any duplicate counts
## That's what this line of code does. It creates another dataframe (df2) in which it has aggregated 
## any duplications into a single count value by adding them together


df2 = data.groupby(["collectDate", 'siteID', 'scientificName' ],as_index=False).agg({'individualCount' : "sum"})

##Now to check that that actually happened. All the values here should be 1

No_dups = df2.pivot_table(index=["collectDate",'siteID'], columns= 'scientificName', values='individualCount', aggfunc=len)


##So now that we've done that, we can make the table we want. Here I've made it so that 
##the index (rows) are the 'plotID','setDate', 
##the columns are the 'taxonID' (kind of a proxy for OTUS in the skbio package but we could use another- your call)
##and the values are the individual counts. 

biodiv_data = df2.pivot(index=["collectDate",'siteID'], columns= 'scientificName', values='individualCount')

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


#### Number of species per site -- this makes a list of values entitled "adiv_obs_otus" which is the number of species at each sampling point as known as species richness
from skbio.diversity import alpha_diversity
adiv_obs_otus = alpha_diversity('observed_otus', array, ids)
adiv_obs_otus

## Shannon's for each site
from skbio.diversity import alpha_diversity
shannon= alpha_diversity('shannon', array, ids)



###Now that you've 

# Calling DataFrame constructor on list with index named by state
obs_otus = pandas.DataFrame(adiv_obs_otus, index= biodiv_data0.index, columns =["richness"] )
obs_otus

shannon_df = pandas.DataFrame(shannon, index= biodiv_data0.index, columns =['shannon'] )
shannon_df

#merge dataframes by index
mergedDf = obs_otus.merge(shannon_df, left_index=True, right_index=True)

#make index a column
mergedDf.reset_index(inplace=True)


##Remove -0 shannons
mergedDf.drop(mergedDf.index[mergedDf['shannon'] == -0], inplace = True)

mergedDf.to_csv('/Users/Jen/Downloads/inv_counts.csv', index = False)

## Averages for each site
rich_mean = mergedDf.groupby(['siteID']).agg({'richness': ['mean', 'min', 'max']})

print(rich_mean)

shannon_mean = mergedDf.groupby(['siteID']).agg({'shannon': ['mean', 'min', 'max']})

print(shannon_mean)

df.to_csv(r'Path where you want to store the exported CSV file\File Name.csv', index = False)

###ANOVAs & box plots
##richness by site-- ### You can also do this for Shannon and by year--
import scipy.stats as stats
stats.f_oneway(mergedDf["shannon"][mergedDf['siteID'] == 'BARC'],
               mergedDf["shannon"][mergedDf['siteID'] == 'FLINT'],
               mergedDf["shannon"][mergedDf['siteID'] == 'MAYF'])


from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(endog=mergedDf["shannon"],groups = mergedDf['siteID'], alpha=0.05)
print(tukey)


import seaborn as sb
import matplotlib.pyplot as plt

ay= sb.catplot(x="siteID", y="richness", kind="box", data=mergedDf) 
ay= sb.stripplot(x="siteID", y="richness", data=mergedDf,  color=".4") 

