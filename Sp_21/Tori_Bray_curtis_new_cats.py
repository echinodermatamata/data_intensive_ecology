#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:33:16 2021

@author: Jen
"""

### Standard loading of libraries
import pandas

import numpy

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

### this is an ANOVA comparing the 4 different groups we made 
## You can see by the output table that overall, there isn't a significant difference between groups, but
## where we really expect there to be a difference there might be, so we do an additional test

from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(endog=data['Bray_curtis'], groups=data['Comp'], alpha=0.05)
print(tukey)

### Here what you're seeing is a tukey test between groups within an ANOVA
### In the results table what you see is that there is a significant difference between Burn/ Burn and Non/Non 
### Which is what we expect!!! Yeah!!!

