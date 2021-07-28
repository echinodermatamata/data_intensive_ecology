
## ----load-packages------------------------------------------------------------------------
# Load packages required for entire script. 
# library(PackageName)  # purpose of package
library(ggplot2)   # efficient, pretty plotting - required for qplot function

# set working directory to ensure R can find the file we wish to import
setwd("~/Desktop/Data_Intensive_Ecology_2021/")

# Load csv file of daily meteorological data from Harvard Forest
harMet.daily <- read.csv(
  file="NEON-DS-Met-Time-Series/HARV/FisherTower-Met/hf001-06-daily-m.csv",
  stringsAsFactors = FALSE
)

####---- some useful code:




