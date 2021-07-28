# load packages
library(neonUtilities)
library(geoNEON)
library(raster)

install.packages("parallel")

library(parallel)



# Set global option to NOT convert all character variables to factors
options(stringsAsFactors=F)

#Site management and event reporting is DP1.10111.001, SITE-- to download for multiple sites, you must make them a vector using c (LIST OF SITES)
data <- loadByProduct(dpID="DP1.10072.001", site= "OSBS",
                      package="expanded", check.size=T)


names(data)

####
View(data$)
######
write.csv(data$mam_pertrapnight, 
          "~/Downloads/mam_pertrapnight.csv", 
          row.names=F)

write.csv(data$variables_10041, 
          "~/Downloads/PATH_variables.csv", 
          row.names=F)





####################################################

data2 <- loadByProduct(dpID="DP1.10041.001", site= c ("LENO", "DELA", "MLBS", "GRSM", "JERC", "DSNY", "OSBS", "ORNL", "TALL", "BLAN", "SERC", "SCBI"), 
                      package="basic", check.size=T)

data2 <- stackByTable("~/Downloads/NEON_temp-air-single 2.zip")

load("~/Downloads/NEON_temp-air-single 2/stackedFiles/SAAT_30min.csv")

names(data2)

####
View(data$)
######
write.csv(data2$mos_pathogenresults, 
          "~/Downloads/mos_pathogenresults.csv", 
          row.names=F)

write.csv(data2$variables_10043, 
          "~/Downloads/mos_counts_variables.csv", 
          row.names=F)
#############################################################




View(data$)
######
write.csv(data$ 
          "~/Downloads/mos_counts.csv", 
          row.names=F)

write.csv(data$variables_, 
          "~/Downloads/mos_counts_variables.csv", 
          row.names=F)





saat<-loadByProduct(dpID="DP1.00002.001", site="SCBI", 
                    startdate="2018-01", enddate="2018-12", 
                  
                    token = Sys.getenv("NEON_TOKEN"),
                    check.size = F)
names(data)

####
View(data$mos_expertTaxonomistIDProcessed)
######
write.csv(data$SAAT_30min, 
          "~/Downloads/SAAT_30min.csv", 
          row.names=F)

write.csv(data$variables_00002, 
          "~/Downloads/SAAT_30min_variables_00002.csv", 
          row.names=F)
