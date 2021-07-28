## Here is the code for this module. I'm using my example file called brd. You need to change the file name, working directory and variable names to match your dataset

setwd("~/Desktop/Data_Intensive_Ecology_2021/")

## In the video they "load" an R dataset. Our data is in .csv format NOT RData, so we need to use the read.csv command. 
#Sorry for the confusion
read.csv("brd_countdata.csv", header= TRUE)

brd <- read.csv("brd_countdata.csv")
View(brd)

##You can do this to make working directly from the video easier

data <- brd
 ## now you should have an entry called "data" in your global environment


## installing packages-- you only need to do this install step one time

install.packages("descr")
install.packages("Hmisc")

## do this every time you go run this program
library(descr)
library(Hmisc)

## The video then goes into how to change the names of the variables in the original data set. This may be something that you want to do. If so use the following function:
label(data$siteID) <- "Site Name"

## making a frequency table
freq(data$siteID)
freq (data$taxonID)

## add cumulative percent to table
freq(as.ordered(data$siteID))

## making a data subset-- don't forget that comma at the end- it will give you an error message that reads "undefined columns selected"

sub1 <- data[data$siteID == 'ABBY',]

View(data$siteID)




###################################
##Data Management Module

## missing data
## code of taking a subset of the data by plot, then replacing native status so the birds coded as UNK is now NaN


### possible things I may need to code for with this data-- year, month and season-- do I want to create a new variable that captures this info? 
##Things to take into consideration when doing that- are there multiple counting days within the same month- This could be a problem if there are 
## counts of the same species in both of those sets...
## what I need to do first is set-up more advanced freq tables


## Making a frequency table with 2 variables 

attach(data)
mytable <- table(data$siteID, data$taxonID) # the first variable is the rows (in this case data$siteID) and the second is the columns (data$taxonID).
mytable

margin.table(mytable, 1) # A frequencies (summed over B)
margin.table(mytable, 2) # B frequencies (summed over A)

prop.table(mytable) # cell percentages
prop.table(mytable, 1) # row percentages
prop.table(mytable, 2) # column percentages

#can also use crosstable function in  
