# Datasets
In this page we describe the methodology and sources used to extract the various datasets provided in this GitHub repository.

## Meteorological Data

### (Dataset Name - Temperature and precipitation)

This dataset provides data about (type of data) measured by more than (number) meteorological stations around the world.

(A nice plot of the position of the stations on a map would be a nice to have!)

#### Sources
We sourced the data from the National Centers for Environmental Information (ncdc.noaa.gov).

* Menne, M.J., I. Durre, B. Korzeniewski, S. McNeal, K. Thomas, X. Yin, S. Anthony, R. Ray,
R.S. Vose, B.E.Gleason, and T.G. Houston, 2012: Global Historical Climatology Network -
Daily (GHCN-Daily), Version 3. [indicate subset used following decimal,
e.g. Version 3.12].
NOAA National Climatic Data Center. http://doi.org/10.7289/V5D21VHZ [2020].

(Find out correct versions)

#### Sourcing Process
There are two ways to obtain the needed data from the source: File Protocol Transfer or the API offered from the source.

We obtain the file containing the full list of available stations via FTP (as this information is not available via API) and use
this to select the desired stations and retrieve the relevant meteorological data. This we provide functions to do this both through
FTP and the API.

#### Filtering and Aggregation
Only data starting from the date provided from the user and from the countries selected from the user is produced in the output dataset.
Missing values are not dropped.

#### Data Description
The output dataset contains the following data

| Column | Description |
| ------ | ----------- |
|        |             |

## Granular Contagion Data

**Pending**

## Demographic Data

**Pending**

## Social Distancing Measures

**Pending**
