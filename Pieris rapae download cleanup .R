library(tidyverse)
library(janitor)


setwd("~/Downloads")
occurrence <- read_csv("~/Downloads/UK_1960_2021/occurrence.csv")

multimedia <- read_csv("~/Downloads/UK_1960_2021/multimedia.csv")


glimpse(occurrence)
glimpse(multimedia)


UK_1960_2021 <- merge (x= multimedia, y=occurrence, by = "coreid") %>%
  clean_names()

glimpse(UK_1960_2021)

UK_1960_2021 <- UK_1960_2021 %>% select(c(coreid,ac_access_uri,dwc_scientific_name, idigbio_event_date,dwc_continent,dwc_country,dwc_county,dwc_state_province))

glimpse(UK_1960_2021)


UK_1960_2021 <- UK_1960_2021 %>% rename(c(image_url= "ac_access_uri",scientific_name = "dwc_scientific_name", collection_date = "idigbio_event_date",continent= "dwc_continent", country="dwc_country", county = "dwc_county", state_province = "dwc_state_province"))

glimpse(UK_1960_2021)

write_csv(UK_1960_2021, "UK_1960_2021.csv")
