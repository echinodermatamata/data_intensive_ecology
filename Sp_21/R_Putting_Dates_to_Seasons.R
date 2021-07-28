
setwd("~/Downloads/")
data <- read.csv ("superparent.csv")

colnames(data)

library(dplyr)
library(tidyverse)

data <- data %>% mutate(season =
                     case_when(month == 1 ~ "W", 
                               month == 2 ~ "W",
                               month == 3 ~ "Sp",
                               month == 4 ~ "Sp", 
                               month == 5 ~ "Sp",
                               month == 6 ~ "Su",
                               month == 7 ~ "Su", 
                               month == 8 ~ "Su",
                               month == 9 ~ "F",
                               month == 10 ~ "F", 
                               month == 11 ~ "F",
                               month == 12 ~ "W")
)
colnames(data)
write.csv(data, 
          "~/Downloads/superparent.csv", 
          row.names=F)