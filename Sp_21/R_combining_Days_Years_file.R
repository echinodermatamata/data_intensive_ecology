library(tidyverse)
library(lubridate)

setwd("~/Downloads/")
data <- read.csv("mos_counts(1).csv")

class(data$collectDate)

data$collectDate <-as.Date(data$collectDate, format = "%m/%d/%Y %H:%M")


class(data$collectDate)

data <- data %>%
  mutate(
    month = collectDate %>% 
      lubridate::as_date() %>% 
      lubridate::month())

data <- data %>%
  mutate(
    year = collectDate %>% 
      lubridate::as_date() %>% 
      lubridate::year())

data <- data %>%
  mutate(
    day = collectDate %>% 
      lubridate::as_date() %>% 
      lubridate::day())


data$month <- as.character(data$month)
data$year <- as.character(data$year)
data$day <- as.character(data$day)

combo = mutate(data,
               concated_column = paste(year, month, day, sep = '_'))




write.csv(combo, 
          "~/Downloads/mos_processed.csv", 
          row.names=F)
