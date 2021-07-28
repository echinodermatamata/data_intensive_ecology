###################################
########### Disclaimer ############
This is the most recent readme publication based on all site-date combinations used during stackByTable.
Information specific to the query, including sites and dates, has been removed. The remaining content reflects general metadata for the data product.
All files used during stacking are listed at the bottom of this document, which includes the data publication dates.
##################################

This data package been produced by and downloaded from the National Ecological Observatory Network, managed cooperatively by Battelle. These data are provided under the terms of the NEON data policy at http://data.neonscience.org/data-policy. 

DATA PRODUCT INFORMATION
------------------------

ID: NEON.DOM.SITE.DP1.10055.001

Name: Plant phenology observations

Description: Phenophase status and intensity of tagged plants

NEON Science Team Supplier: TOS

Abstract: This data product contains the quality-controlled, native sampling resolution data from in-situ observations of plant leaf development and reproductive phenophases, at each of NEON's terrestrial sites. Phenophase status and intensity definitions follow those of the USA National Phenology Network (USA-NPN).  Status and intensity data are reported per phenophase per individual or patch, for each day observed. For additional details, see the user guide, protocols, and science design listed in the Documentation section in this data product's details webpage.

Latency:
The expected time from data and/or sample collection in the field to data publication is as follows, for each of the data tables (in days) in the downloaded data package. See the Data Product User Guide for more information.

phe_perindividual:  30

phe_perindividualperyear:  30

phe_statusintensity:  30

Brief Design Description: Approximately 90 individual plants or plant patches are monitored at each site. Individuals of 3 dominant species at each site are targeted for monitoring during initial operations. Sampling intervals vary seasonally, ranging from 2-3x weekly during periods of rapid phenological transition to much less frequently during other times of year. NEON employs status-based monitoring in which the phenological condition of an individual is reported any time that individual is observed.

Brief Study Area Description: Plant phenology is monitored at NEON terrestrial sites, typically within the tower airshed.

Keywords: leaves, green-up, seasonality, leaf, senescence, plants, flower, phenology, phenophase, timing


DATA PACKAGE CONTENTS
---------------------

This data product contains up to 3 data tables:

phe_perindividual - Geolocation and taxonomic identification for phenology plants
phe_perindividualperyear - Annual census of size and disease status on phenology plants
phe_statusintensity - Plant phenophase status and intensity data
If data are unavailable for the particular sites and dates queried, some tables may be absent.
Basic download package definition: The basic data package includes all measurements. An expanded download package is not available for this product.

FILE NAMING CONVENTIONS
-----------------------

NEON data files are named using a series of component abbreviations separated by periods. File naming conventions for NEON data files differ between NEON science teams. A file will have the same name whether it is accessed via the data portal or the API.

NEON observational systems (OS) data files: NEON.DOM.SITE.DPL.PRNUM.REV.DESC.YYYY-MM.PKGTYPE.GENTIME.csv

The definitions of component abbreviations are below. See NEON.DOC.002651: NEON Data Product Numbering Convention, located at http://data.neonscience.org/documents for more information.

General conventions, used for all data products:
   NEON: denotes the organizational origin of the data product and identifies the product as operational; data collected as part of a special data collection exercise are designated by a separate, unique alphanumeric code created by the PI.

   DOM: a three-character alphanumeric code, referring to the domain of data acquisition (D01 - D20).

   SITE: a four-character alphanumeric code, referring to the site of data acquisition; all sites are designated by a standardized four-character alphabetic code.

   DPL: a three-character alphanumeric code, referring to data product processing level;

   PRNUM: a five-character numeric code, referring to the data product number (see the Data Product Catalog at http://data.neonscience.org/data-product-catalog).

   REV: a three-digit designation, referring to the revision number of the data product. The REV value is incremented by 1 each time a major change is made in instrumentation, data collection protocol, or data processing such that data from the preceding revision is not directly comparable to the new.

   HOR: a three-character designation, referring to measurement locations within one horizontal plane. For example, if five surface measurements were taken, one at each of the five soil array plots, the number in the HOR field would range from 001-005. 

   VER: a three-character designation, referring to measurement locations within one vertical plane. For example, if eight air temperature measurements are collected, one at each tower vertical level, the number in the VER field would range from 010-080. If five soil temperature measurements are collected below the soil surface, the number in the VER field would range from 501-505. 

   TMI: a three-character designation, referring to the temporal representation, averaging period, or coverage of the data product (e.g., minute, hour, month, year, sub-hourly, day, lunar month, single instance, seasonal, annual, multi-annual). 000 = native resolution, 001 = native resolution (variable or regular) or 1 minute, 002 = 2 minute, 005 = 5 minute, 015 = 15 minute, 030 = 30 minute, 060 = 60 minutes or 1 hour, 100 = approximately once per minute at stream sites and once every 5-10 minutes at buoy sites (lakes/rivers), 101-103 = native resolution of replicate sensor 1, 2, and 3 respectively, 999 = Sensor conducts measurements at varied interval depending on air mass, 01D = 1 day, 01M = 1 month, 01Y = 1 year.

   DESC: an abbreviated description of the data file or table.

   YYYY-MM: the year and month of the data in the file.

   PKGTYPE: the type of data package downloaded. Options are 'basic', representing the basic download package, or 'expanded',representing the expanded download package (see more information below).

   GENTIME: the date-time stamp when the file was generated, in UTC. The format of the date-time stamp is YYYYMMDDTHHmmSSZ.

Time stamp conventions:
   YYYY: Year
   YY: Year, last two digits only
   MM: Month: 01-12
   DD: Day: 01-31
   T: Indicator that the time stamp is beginning
   HH: Hours: 00-23
   mm: Minutes: 00-59
   SS: Seconds: 00-59
   Z: Universal Time Coordinated (Universal Coordinated Time), or UTC

ADDITIONAL INFORMATION
----------------------

Data products that are a source of this data product:

Data products that are derived from this data product:

Other related data products (by sensor, protocol, or variable measured):
NEON.DOM.SITE.DP1.00033.001, Phenology images
NEON.DOM.SITE.DP1.00042.001, Snow depth and understory phenology images

Protection of species of concern: At most sites, taxonomic IDs of species of concern have been 'fuzzed', i.e., reported at a higher taxonomic rank than the raw data, to avoid publishing locations of sensitive species. For a few sites with stricter regulations (e.g., Great Smoky Mountains National Park (GRSM)), records for species of concern are not published. 

Obfuscation of Personnel Information: At times it is important to know which data were collected by particular observers. In order to protect privacy of NEON technicians while also providing a way to consistently identify different observers, we obfuscate each NEON personnel name by internally linking it to a unique string identifier (e.g., Jane Doe=ByrziN0LguMJHnInl2NM/trZeA5h+c0) and publishing only the identifier.

CHANGE LOG
----------

Issue Date: 2017-07-27
Issue: As part of NEON's ongoing construction tasks, the processing pipeline for most data products for NEON's observational systems (terrestrial [TOS] and aquatic [AOS]) has been simplified to use a generic codebase.
       Date Range: 2017-07-27 to 2017-07-27
       Location(s) Affected: All
Resolution Date: 2017-07-27
Resolution: Data that were published previously have been reprocessed and republished using the generic code -- replacing data that had been processed using the original algorithms described in Algorithm Theoretical Basis Documents (ATBDs). Consequently, data are in a new format including, in many cases, different data fields. Details of the new processing pipeline can be found in http://data.neonscience.org/api/v0/documents/OS_generic_transitions_vA  and http://data.neonscience.org/api/v0/documents/Nicl_Language_DRAFT.

ADDITIONAL REMARKS
------------------

Queries for this data product will return data from all dates for `phe_perindividual` (which may be tagged for sampling many years before a phenology observation), whereas `phe_perindividualperyear` and `phe_statusintensity` files will be subset to data collected during the date range specified. The protocol dictates that each individual is established once (one expected record per individualID in `phe_perindividual` from initial establishment), but additional records in `phe_perindividual` for a given individualID may occur when subsequent visits determine an update to the taxonomic identification or relative position is warranted. Each actively monitored individual is intended to be measured once per year for size and disease status, leading to one record in `phe_perindividualperyear` per calendar year for each individualID in `phe_perindividual`. Individuals that have died or otherwise been dropped for monitoring may have 0 records in `phe_perindividualperyear`. An record from `phe_perindividual` may have zero or one child records in `phe_statusintensity` per date (local time), depending on the date range of the data downloaded; a given `phe_perindividual.individualID` is expected to be sampled for phenophase status and intensity a maximum of once per day. Duplicates may exist where protocol and/or data entry aberrations have occurred; users should check data carefully for anomalies before joining tables. Taxonomic IDs of species of concern have been 'fuzzed'; see data package readme files for more information.

NEON DATA POLICY AND CITATION GUIDELINES
----------------------------------------

Please visit http://data.neonscience.org/data-policy for more information about NEON's data policy and citation guidelines.

DATA QUALITY AND VERSIONING
---------------------------

The data contained in this file are considered provisional. Updates to the data, QA/QC and/or processing algorithms over time will occur on an as-needed basis.  Please check back to this site for updates tracked in change logs.  Query reproducibility on provisional data cannot be guaranteed. 
 
Starting in 2020 or earlier, NEON will begin to offer static versions of each data product, annotated with a globally unique identifier. Versioned IS and OS data will be produced by reprocessing each IS and OS data product from the beginning of the data collection period to approximately 12-18 months prior to the reprocessing date (to allow for calibration checks, return of external lab data, etc.). The reprocessing step will use the most recent QA/QC methods and processing algorithms. Versioned AOP data will be produced by reprocessing the entire AOP archive as advances in algorithms and processing technology are incorporated. This will typically occur in the northern winter months, between flight season peaks, and will be on the order of every 3 to 5 years in frequency.

POST STACKING README DOCUMENTATION
----------------------------------

Each row contains the readme filename used during stackByTable

NEON.D02.BLAN.DP1.10055.001.readme.20200511T150845Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T151012Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T151106Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T151500Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T151003Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T151026Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T150802Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142330Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142502Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142518Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142214Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T150955Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T151112Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T151443Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T150934Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T151044Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T150808Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142326Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142338Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142930Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142208Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142902Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T151118Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T151430Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T150945Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T151033Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T150812Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142446Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142923Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142350Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142445Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142422Z.txt
NEON.D02.BLAN.DP1.10055.001.readme.20200511T142310Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T151109Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150923Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150744Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150616Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150240Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150138Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150008Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150650Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150443Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150332Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T145037Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150910Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150756Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150629Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150248Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150124Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150014Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150635Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150426Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150343Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T145041Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150605Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150227Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150107Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T145956Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150630Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150432Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T150336Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T145046Z.txt
NEON.D02.SCBI.DP1.10055.001.readme.20200511T145022Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T141225Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140754Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140827Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140923Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140828Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140336Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140434Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140444Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140051Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140131Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T141352Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140811Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140812Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140834Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140944Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140446Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140404Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140529Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140002Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140009Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140015Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140735Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140758Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140841Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140844Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140402Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140408Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140121Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140134Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140305Z.txt
NEON.D02.SERC.DP1.10055.001.readme.20200511T140000Z.txt
