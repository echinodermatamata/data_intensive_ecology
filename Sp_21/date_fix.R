data <-read.csv("~/Downloads/OSBSm.csv")


### GOT IT!
library(lubridate)

## This is the important line you need. It makes the collectDate recognizable as a mdy data by R
data$collectDate <- as.Date(mdy(data$collectDate))


##Now this runs fine
data <- data %>%
  mutate(
    year = collectDate %>% 
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