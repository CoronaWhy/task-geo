# Spainish Covid 19 cases on regional level

## General information

- **Description**: Daily counts of covid 19 in each of the Spanish autonomous communities.
- **Credits**: Spain Ministry of Health.
- **Source**: https://covid19.isciii.es/resources/serie_historica_acumulados.csv.

The daily counts data is also enriched with [statistical data about the autonomous communities](https://en.wikipedia.org/wiki/Autonomous_communities_of_Spain), retrieved Apr 2020

## Column Details

**country**
- description: country name
- type: str

**autonomous_community_iso**
- description: iso code

**area_km_squared**
- description: area of automonous community
- type: float
- units: km**2

**population**
- description: population of automonous community
- type: float

**gdp_per_capita_euros**
- description: gross domestic product per person
- type: float
- units: euros

**density_pop_per_km_squared**
- description: population density
- type: float
- units: number of people per km**2

**date**
- description: date corresponding to the datapoint
- type: date

**hospitalized**
- description: number of people in hospital due to covid19
- type: float

**icu**
- description: number of people in intensive care unit due to covid19
- type: float

**deceased**
- description: number of people died due to covid19
- type: float

**recovered**
- description: number of people who have recovered from covid19
- type: float

## Transformations applied

- converting the cumulative daily counts to raw daily counts
- all NaNs in these columns:  'cases', 'hospitalized', 'icu', 'deceased', 'recovered' are replaced by 0
- the raw daily count data is merged with the statistical data on matching autonomous region iso code

