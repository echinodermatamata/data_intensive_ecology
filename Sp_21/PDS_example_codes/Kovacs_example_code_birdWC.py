# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


"""
#import libraries -- do this each time when loading the program

import pandas

import numpy

#in this example I am working with a data file named birdWC. You should change this to work with your particular data file 

birdWC = pandas.read_csv('brd_countdata.csv', low_memory = False)

#lower-case all column names inthe data file- you can make this upper case too. This is good for the NEON dataset because they have weird uppercase lower case combos

birdWC.columns = map(str.lower, birdWC.columns)

# bug fix for display formats to avoid run time errors

pandas.set_option('display.float_format', lambda x:'%f'%x)



print(len(birdWC)) # tells you number of observations in data set (rows)
print(len(birdWC.columns)) # tells you number of variables (columns)

# Another way to see rows in a dataframe
print(len(birdWC.index))

#My variable values are NOT numeric in this case, they are character therefore I did not convert to numeric, BUT if I had to:
   #to run this code- just remove the #
    #birdWC["VARIABLE"] = birdWC["VARIABLE"].convert_objects(convert_numeric=True)

 #Thinking about descrptive stats for a dataset-- FREQUENCIES AND COUNTS
 #here we're just looking at Counts and percentages-- see crosstab function below for making a crosstabs figure
   
print("Number of Observations per Site")
sitecount = birdWC["siteid"].value_counts(sort=False, dropna = False)
print (sitecount)

print("Percentage of Observations per Site")
siteper = birdWC["siteid"].value_counts(sort=False, normalize= True, dropna = False)
print(siteper)

print("Number Bird Taxons Oberved")
taxoncount = birdWC["taxonid"].value_counts(sort=False, dropna = False)
print (taxoncount)


print("Percentage Bird Taxons Oberved")
taxonper = birdWC["taxonid"].value_counts(sort=False, normalize= True, dropna = False)
print(taxonper)


#Alternatively

sitecount1 = birdWC.groupby("siteid").size()
print(sitecount1)

siteper1 = birdWC.groupby("siteid").size()*100/len(birdWC)
print(siteper1)

siteper.to_csv("new_data.csv")

#taking a subset, so say I only wanted to look at native bird species in my dataset. If I wanted to further subset I could add things in using & (birdWC['nativestatuscode'] == "N")

subnat = birdWC[(birdWC['nativestatuscode'] == "N")]

#Making a table to submit in Canvas- this makes an html figure which you can save OR copy and paste into Canvas

sitecount = pandas.crosstab(index=birdWC["siteid"],  # Make a crosstab which makes a dataframe rather than a series
                              columns="count")      # Name the count column

sitecount

sitecount.to_html() # when you execute this line it prints the html code in your console window.
# you can copy this code from the console and put it in Canvas by choosing "insert" "embed" and pasting the code

sitecount.to_html("sitecount.html") #saves an html file to your working directory which you can copy paste or link to 


#To put PROPORTIONS in a frequency table

siteper= pandas.crosstab (index= birdWC["siteid"], columns= "proportions").apply (lambda r: r/len (birdWC["siteid"]), axis =1)  # Make a crosstab which makes a dataframe rather than a series
                              

siteper


siteper.to_html() # when you execute this line it prints the html code in your console window.
# you can copy this code from the console and put it in Canvas by choosing "insert" "embed" and pasting the code

siteper.to_html("sitecount.html") #saves an html file to your working directory which you can copy paste or link to 


##############################################################
##  DATA MANAGEMENT MODULE  ---  NEW MODULE 

## missing data
## code of taking a subset of the data by plot, then replacing native status so the birds coded as UNK is now NaN

subplot = birdWC[(birdWC['siteid'] == "SJER") & (birdWC['plotid'] == "SJER_034")]
sub1=subplot.copy()

sub1['nativestatuscode']= sub1['nativestatuscode'].replace("UNK",numpy.nan)  #replaces missing value

print("Native Status for SJER sub 034")
c1= sub1['nativestatuscode'].value_counts(sort=False,dropna=False) # dropna shows nan data
print(c1)


### possible things I may need to code for with this data-- year, month and season-- do I want to create a new variable that captures this info? 
##Things to take into consideration when doing that- are there multiple counting days within the same month- This could be a problem if there are 
## counts of the same species in both of those sets...
## what I need to do first is set-up more advanced freq tables


## Making a frequency table with 2 variables 

site_date= pandas.crosstab (index = birdWC["startdate"], columns= birdWC["siteid"], margins=True)

## I could even do this with 3 variables-- not really what I need to do with this set, but in case you do....

site_date= pandas.crosstab (index = birdWC["startdate"], columns= [birdWC["nativestatuscode"], birdWC["siteid"]], margins=True)


###website for crosstabs examples for tables: http://hamelg.blogspot.com/2015/11/python-for-data-analysis-part-19_17.html


#####Notes to myself: I need to find a way to split up the dates and times for some of the NEON sets and do biodiveristy calculations.
#### Need to get students their datasets



