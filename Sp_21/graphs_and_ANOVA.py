#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:14:47 2021

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





data= pandas.read_csv('superparent.csv', low_memory = False)


list(data)


##My graphs cheat sheet: https://seaborn.pydata.org/tutorial.html
## it includes a section on color and palette and all that fun stuff too. 
import seaborn as sns

## so a basic graph

sns.catplot(x="season", y="specificConductance", hue="aquaticSiteType", kind="box", data=data)



###here's one where you layer a scatterplot over a box graph

###here's one where you layer a scatterplot over a box graph

g= sns.catplot(x="aquaticSiteType", y="specificConductance", kind="box", data=data)
g= sns.stripplot(x="aquaticSiteType", y="specificConductance", data=data, color=".3")

#### And a quick ANOVA ## you may not need this particular analysis, but I wanted to give it 
##to you so you could see how it looks
import scipy.stats as stats

stats.f_oneway(data["specificConductance"][data['aquaticSiteType'] == 'lake'],
               data['specificConductance'][data['aquaticSiteType'] == 'river'],
              data['specificConductance'][data['aquaticSiteType'] == 'stream'])

### you can see that there is a ridiculusly significant difference between these values
### like e-29 signficant



## The next step is to see which of the comparisions, if not all, are significant. 
## so we run a Tukeys  HSD-- and look at the table

from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(endog=data['specificConductance'], groups=data['aquaticSiteType'], alpha=0.05)
print(tukey)

## and see that lake and river are signficantly different from each other and river and stream are, but
## lake and stream are not, which adds up to what we see in the graph. 

###More stats stuff in python if you need it: 
    ##  https://scipy-lectures.org/packages/statistics/index.html