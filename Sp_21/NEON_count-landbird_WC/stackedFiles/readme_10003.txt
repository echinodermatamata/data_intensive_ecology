###################################
########### Disclaimer ############
This is the most recent readme publication based on all site-date combinations used during stackByTable.
Information specific to the query, including sites and dates, has been removed. The remaining content reflects general metadata for the data product.
All files used during stacking are listed at the bottom of this document, which includes the data publication dates.
##################################

This data package been produced by and downloaded from the National Ecological Observatory Network (NEON). NEON is funded by the National Science Foundation (Awards 0653461, 0752017, 1029808, 1138160, 1246537, 1638695, 1638696, 1724433) and managed cooperatively by Battelle. These data are provided under the terms of the NEON data policy at https://www.neonscience.org/data-policy.

DATA PRODUCT INFORMATION
------------------------

ID: NEON.DOM.SITE.DP1.10003.001

Name: Breeding landbird point counts

Description: Count, distance from observer, and taxonomic identification of breeding landbirds observed during point counts

NEON Science Team Supplier: Terrestrial Observation System

Abstract: This data product contains the quality-controlled, native sampling resolution data from NEON's breeding landbird sampling. Breeding landbirds are defined as “smaller birds (usually exclusive of raptors and upland game birds) not usually associated with aquatic habitats” (Ralph et al. 1993). The breeding landbird point counts product provides records of species identification of all individuals observed during the 6-minute count period, as well as metadata which can be used to model detectability, e.g., weather, distances from observers to birds, and detection methods. The NEON point count method is adapted from the Integrated Monitoring in Bird Conservation Regions (IMBCR): Field protocol for spatially-balanced sampling of landbird populations (Hanni et al. 2017; http://bit.ly/2u2ChUB). For additional details, see protocol [NEON.DOC.014041](http://data.neonscience.org/api/v0/documents/NEON.DOC.014041vF): TOS Protocol and Procedure: Breeding Landbird Abundance and Diversity and science design [NEON.DOC.000916](http://data.neonscience.org/api/v0/documents/NEON.DOC.000916vB): TOS Science Design for Breeding Landbird Abundance and Diversity.

Latency: The expected time from data and/or sample collection in the field to data publication is as follows, for each of the data tables (in days) in the downloaded data package. See the Data Product User Guide for more information.
 
brd_countdata: 120

brd_perpoint: 120

brd_personnel: 120

brd_references: 120

Brief Design Description: Depending on the size of the site, sampling for this product occurs at either randomly distributed individual points or grids of nine points each. At larger sites, point count sampling occurs at five to ten 9-point grids, with grid centers collocated with distributed base plot centers (where plant, beetle, and/or soil sampling may also occur), if possible. At smaller sites (i.e., sites that cannot accommodate a minimum of 5 grids) point counts occur at the southwest corner (point 21) of 5-25 distributed base plots. Point counts are conducted once per breeding season at large sites and twice per breeding season at smaller sites. Point counts are six minutes long, with each minute tracked by the observer, following a two-minute settling-in period. All birds are recorded to species and sex, whenever possible, and the distance to each individual or flock is measured with a laser rangefinder, except in the case of flyovers.

Brief Study Area Description: This sampling occurs at all NEON terrestrial sites.

Keywords: avian, distance sampling, vertebrates, taxonomy, invasive, community composition, species composition, population, Aves, diversity, native, landbirds, introduced, animals, point counts, Chordata, Animalia, birds


DATA PACKAGE CONTENTS
---------------------

This data product contains up to 4 data tables:

brd_perpoint - Per point metadata for breeding landbirds
brd_personnel - Personnel conducting breeding landbird point count data and quiz scores
brd_references - Identification references used to identify birds, by site and year
brd_countdata - Point count data for breeding landbirds
If data are unavailable for the particular sites and dates queried, some tables may be absent.
Basic download package definition: The basic package contains the per point metadata table that includes data pertaining to the observer and the weather conditions and the count data table that includes all of the observational data.

Expanded download package definition: The expanded package includes two additional tables and two additional fields within the count data table. The personnel table provides institutional information about each observer, as well as their performance on identification quizzes, where available. The references tables provides the list of resources used by an observer to identify birds. The additional fields in the countdata table are family and nativeStatusCode, which are derived from the NEON master list of birds.

FILE NAMING CONVENTIONS
-----------------------

NEON data files are named using a series of component abbreviations separated by periods. File naming conventions for NEON data files differ between NEON science teams. A file will have the same name whether it is accessed via NEON's data portal or API. Please visit https://www.neonscience.org/data-formats-conventions for a full description of the naming conventions.

ISSUE LOG
---------

This log provides a list of issues that were identified during data collection or processing, prior to publication of this data package. For a more recent log, please visit this data product's detail page at https://data.neonscience.org/data-products/DP1.10003.001.

Issue Date: 2020-10-28
Issue: There was not a way to indicate that a scheduled sampling event did not occur.
       Date Range: 2013-01-01 to 2020-01-01
       Location(s) Affected: All
Resolution Date: 2020-01-01
Resolution: The fields samplingImpracticalRemarks and samplingImpractical were added prior to the 2020 field season. The contractor supplies the samplingImpracticalRemarks field, and this field autopopulates the samplingImpractical field. The samplingImpractical field has a value other than OK if something prevented sampling from occurring.

ADDITIONAL INFORMATION
----------------------

Queries for this data product will return data collected during the date range specified for `brd_perpoint` and `brd_countdata`, but will return data from all dates for `brd_personnel` (quiz scores may occur over time periods which are distinct from when sampling occurs) and `brd_references` (which apply to a broad range of sampling dates). A record from `brd_perPoint` should have 6+ child records in `brd_countdata`, at least one per pointCountMinute. Duplicates or missing data may exist where protocol and/or data entry aberrations have occurred; users should check data carefully for anomalies before joining tables. Taxonomic IDs of species of concern have been 'fuzzed'; see data package readme files for more information.

Protection of species of concern: At most sites, taxonomic IDs of species of concern have been 'fuzzed', i.e., reported at a higher taxonomic rank than the raw data, to avoid publishing locations of sensitive species. For a few sites with stricter regulations (e.g., Great Smoky Mountains National Park (GRSM)), records for species of concern are not published. 

NEON DATA POLICY AND CITATION GUIDELINES
----------------------------------------

A citation statement is available in this data product's detail page at https://data.neonscience.org/data-products/DP1.10003.001. Please visit https://www.neonscience.org/data-policy for more information about NEON's data policy and citation guidelines.

DATA QUALITY AND VERSIONING
---------------------------

NEON data are initially published with a status of Provisional, in which updates to data and/or processing algorithms will occur on an as-needed basis, and query reproducibility cannot be guaranteed. Once data are published as part of a Data Release, they are no longer provisional, and are associated with a stable DOI.

To learn more about provisional versus released data, please visit https://www.neonscience.org/data-revisions-releases.

POST STACKING README DOCUMENTATION
----------------------------------

Each row contains the readme filename used during stackByTable

NEON.D16.ABBY.DP1.10003.001.readme.20210123T023002Z.txt
NEON.D16.WREF.DP1.10003.001.readme.20210123T023002Z.txt
NEON.D17.SJER.DP1.10003.001.readme.20210123T023002Z.txt
NEON.D17.SOAP.DP1.10003.001.readme.20210123T023002Z.txt
NEON.D17.TEAK.DP1.10003.001.readme.20210123T023002Z.txt
NEON.D18.BARR.DP1.10003.001.readme.20210123T023002Z.txt
NEON.D19.DEJU.DP1.10003.001.readme.20201223T141839Z.txt
NEON.D19.DEJU.DP1.10003.001.readme.20210123T023002Z.txt
NEON.D19.HEAL.DP1.10003.001.readme.20201223T142001Z.txt
NEON.D19.HEAL.DP1.10003.001.readme.20210123T023002Z.txt
