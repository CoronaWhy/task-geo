# GOOGLE MOBILITY REPORTS

## General information

- **Description**: Contains the variations in mobility tracked by Google worldwide.
    The data is presented at both country and region level, with lesser granularity in some cases (US).
- **Credits**: Google.
- **Source**: https://www.google.com/covid19/mobility/

## Description

**country_iso**
- Description: ISO-2 code for the country
- Type: string


**region**
- Description: Name of the region
- Type: string

**date**
- Description: The date the measurements corresponds to
- Type: date.

**retail_recreation**
- Description: Changes in movement for places classified as retail and recreation.
- Type: float

**grocery_pharmacy**
- Description: Changes in movement for places classified as grocery and pharmacy.
- Type: float

**parks**
- Description: Changes in movement for places classified as parks.
- Type: float

**transit_stations**
- Description: Changes in movement for places classified as transit and stations.
- Type: float

**workplaces**
- Description: Changes in movement for places classified as workplaces.
- Type: float

**residential**
- Description: Changes in movement for places classified as residential.
- Type: float


## Transformations applied

The only transformations applied to the original dataset are:
- Renaming of columns
- Casting of values