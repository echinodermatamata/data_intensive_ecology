#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:33:16 2021

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

data = pandas.read_csv('temp.csv', low_memory = False)

print(data.columns)
