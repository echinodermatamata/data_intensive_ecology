library(tidyverse)
library(vegan)
library(readr)
library(tidyverse)
library(vegan)
library(stringr)
library(ggplot2)
library(FSA)
library(neonUtilities)
library(dbplyr)
library(dplyr)

data <-read.csv("~/Desktop/Data_Intensive_Ecology_2021/mos_matrix (1).csv")

##uses dplyr to replace NAs with 0
data0 <- mutate_all(data, ~replace(., is.na(.), 0))

# Convert siteID, year, month, and day to factors
data0$siteID <- as.character(data0$siteID)
data0$year <- as.character(data0$year)
data0$month <- as.character(data0$month)
data0$day <- as.character(data0$day)


##Create a column that combines SiteID, year, month &  day into a single variable name and move to the first column
data0 = mutate(data0,
               concated_column = paste(siteID, year, month, day, sep = '_'))

###This line of code moves concated column to the first column-- it is a conflicted line of code. It works, but needs a fix someday
data0 <- data0 %>%
  data_frame %>% dplyr::select(concated_column, everything())

##take out the year, month, day columns

data0 = subset(data0, select = -c(year, month, day))

### Now to make the "metadata" file that takes the siteID & concated column and joins it with the altitude and temp data

##FIRST read in the .csv file with the site altitude & temp

site <-read.csv("~/Desktop/Data_Intensive_Ecology_2021/Site_info.csv")

##Create a dataframe that is just the siteId and concated_column

site_concated <- subset(data0, select = c(siteID, concated_column))

##Join site & site_concated together by SiteID
# merge two data frames by SiteID
df1 <- site
df2 <- site_concated

## had to do this dumb rename step here for some reason- siteID is now SiteID in both dataframes
df1 %>% rename (SiteID = SiteID)
df2 <- df2 %>% rename (SiteID = siteID)



meta <- left_join(df1,df2, by = "SiteID")
##moved concated_column to first column 
meta <- meta %>%
  data_frame %>% dplyr::select(concated_column, everything())
##renamed concated_column to sampleID

meta <- meta %>% rename (sampleID = concated_column)

##clean-up take out the siteID column in the data0 file

data0 <- subset(data0, select = -(siteID))

#rename concated_column to sample ID in data0

data0 <- data0 %>% rename (sampleID = concated_column)

## Now time to run those stats

library(vegan)

###This line calculates the number of species for each sample. We can then run an ANOVA to ask if mean species richness is significantly different across sites.
sppr <- specnumber(data0)

# analysis of variance takes the same form as the usual models you'd see in R
# response ~ dependent, data = environmental grouping

sppr_aov <- aov(sppr ~ SiteID, data = meta)
summary(sppr_aov)

##Looks like there’s a highly significant difference in species richness between SiteIDs. Let’s plot!

##Need to take that number of species per site list and make it a dataframe
sppr_df <- enframe(sppr, name= NULL, value= "value") 

## Now we're going to add it to the meta dataframe just so we have all of that data together
sppr_df <- cbind (meta,sppr_df)

###Rename value to "species_number"

sppr_df <- sppr_df %>% rename (species_number = value)


## Now we can graph it

p <- ggplot(sppr_df, aes(SiteID, species_number))
p + geom_boxplot()


## We can also do Shannon's Biodiversity Index too
data1 <- subset(data0, select = -(sampleID))
shannondiv <- diversity(data1)

##ANOVA for Shannon's

sppdiv_aov <- aov(shannondiv ~ SiteID, data = meta)
summary(sppdiv_aov)
### Again highly significant, and we can graph it, but first...
##Need to take that Shannon's Number per site list and make it a dataframe
sppdiv_df <- enframe(shannondiv, name= NULL, value= "value") 

## Now we're going to add it to the meta dataframe just so we have all of that data together
sppr_df <- cbind (meta,sppdiv_df)

###Rename value to "diversity"

sppr_df <- sppr_df %>% rename (diversity = value)

p2 <- ggplot(sppr_df, aes(SiteID, diversity))
p2 + geom_boxplot()

## you're going to want to also run some correlations using the sppr_df file that you've created here. 
###If you look at the sspr_df file you will see that you now have the average number of species at each site,
#the average biodiversity index at each site, the average temp, and the latitude.
# You can use this source to look at how to do correlations
## https://scientificallysound.org/2016/04/04/r-pearson-correlation/
##Or the videos in Canvas

## Last bit of code here export the sppr_df file you created as a .csv file in your downloads folder in case you want it for later

write.csv(sppr_df, 
          "~/Downloads/sppr_df.csv", 
          row.names=F)
