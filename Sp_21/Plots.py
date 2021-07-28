#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:17:48 2021

@author: Jen
"""

import pandas

import numpy

### setting my working directory here, because I'm always working out of random folders it seems##
from os import chdir, getcwd
wd=getcwd()
chdir(wd)

import os
os.chdir('/Users/Jen/Desktop')


### loading file###Named it data
data = pandas.read_csv('gwc_fieldSuperParent.csv', low_memory = False)



###Wanted list of column names 
print(data.columns)

import seaborn

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)

sns.catplot(x='aquaticSiteType', y= 'specificConductance', data=data)


sns.catplot(x='aquaticSiteType', y= 'specificConductance', kind="box", data=data)

