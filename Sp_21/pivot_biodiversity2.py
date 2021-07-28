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
os.chdir('/Users/Jen/Desktop/')


### loading file###Named it data
data = pandas.read_csv('mos_expertTaxonomistIDProcessed.csv', low_memory = False)



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

dups = data.pivot_table(index=['plotID','setDate'], columns= 'taxonID', values='individualCount', aggfunc=len)

##Anyway, my solution to this duplication issue is to have Python combine (sum) any duplicate counts
##within a year. That's what this line of code does. It creates another dataframe (df2) in which it has aggregated 
## any duplications into a single count value by adding them together


df2 = data.groupby(['plotID', 'setDate', "taxonID" ],as_index=False).agg({'individualCount' : "sum"})

##Now to check that that actually happened. All the values here should be 1

No_dups = df2.pivot_table(index=['plotID','setDate'], columns= 'taxonID', values='individualCount', aggfunc=len)


##So now that we've done that, we can make the table we want. Here I've made it so that 
##the index (rows) are the dnaSampleID (proxy for year or pre or post burn), 
##the columns are the completeTaxonomy (kind of a proxy for OTUS, but we could use another- your call)
##and the values are the total sequence counts. 

biodiv_data = df2.pivot(index=['plotID','setDate'], columns= 'taxonID', values='individualCount')



biodiv_data0 = biodiv_data.apply (pandas.to_numeric, errors='coerce')
biodiv_data0= biodiv_data.replace(numpy.nan,0)


print (biodiv_data0)
                               
array = biodiv_data0.to_numpy() 

ids= list(biodiv_data0.index)



from skbio.diversity import alpha_diversity
adiv_obs_otus = alpha_diversity('observed_otus', array, ids)
adiv_obs_otus

from skbio.diversity import beta_diversity
bc_dm = beta_diversity("braycurtis", array, ids)
print(bc_dm)
                             