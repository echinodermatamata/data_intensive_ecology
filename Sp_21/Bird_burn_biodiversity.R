install.packages("tidyverse")
install.packages("neonUtilities")
install.packages("vegan")
install.packages("vegetarian")
install.packages("readr")
install.packages("stringr")
install.packages("ggplot2")
install.packages("FSA")

library(tidyverse)
library(vegan)
library(readr)
library(tidyverse)
library(vegan)
library(stringr)
library(ggplot2)
library(FSA)
library(neonUtilities)

data <-read.csv("~/Desktop/Data_Intensive_Ecology_2021/Bird_Burn_Disturbance_Project/brd_countdata.csv")

# extract year from date, add it as a new column
data <- data %>%
  mutate(
    year = startDate %>% 
      lubridate::as_date() %>% 
      lubridate::year())

# extract month from date, add it as a new column
data <- data %>%
  mutate(
    month_year = startDate %>% 
      lubridate::as_date() %>% 
      lubridate::month())

# extract day from date, add it as a new column
data <- data %>%
  mutate(
    day = startDate %>% ###YOU MAY NEED TO CHANGE THIS VARIABLE FOR YOUR DATASET
      lubridate::as_date() %>% 
      lubridate::day())

# Convert plotID and taxonID to factors
data$plotID <- as.factor(data$plotID)
data$taxonID <- as.factor(data$taxonID)
data$siteID <- as.factor(data$siteID)

# Remove columns where targetTaxaPresent = N
# No data associated with them
data <- filter (data, targetTaxaPresent=="Y")





####################################


bird_matrix <- data %>% group_by(siteID, year, month, day, taxonID) %>%
  summarise(count=n()) %>%
  spread(taxonID,count)

# Convert plotID and taxonID to factors
bird_matrix$siteID <- as.character(bird_matrix$siteID)
bird_matrix$year <- as.character(bird_matrix$year)
bird_matrix$month <- as.character(bird_matrix$month)
bird_matrix$day <- as.character(bird_matrix$day)

combo = mutate(bird_matrix,
               concated_column = paste(siteID, year, month, day, sep = '_'))

new_df <- combo %>%
  select(concated_column, everything())

short <- subset(new_df, select=-c(siteID, year, month, day))

number <- specnumber(new_df)




]


