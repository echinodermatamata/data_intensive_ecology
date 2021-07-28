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


# extract year from date, add it as a new column
data <- data %>%
  mutate(
    year = startDate %>% 
      lubridate::as_date() %>% 
      lubridate::year())

# extract month from date, add it as a new column
data <- data %>%
  mutate(
    month = startDate %>% 
      lubridate::as_date() %>% 
      lubridate::month())

# extract day from date, add it as a new column
data <- data %>%
  mutate(
    day = startDate %>% ###YOU MAY NEED TO CHANGE THIS VARIABLE FOR YOUR DATASET
      lubridate::as_date() %>% 
      lubridate::day())