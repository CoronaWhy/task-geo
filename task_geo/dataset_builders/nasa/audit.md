# NASA meteorological data

## General information

- **Description**: This dataset provides time series of meteorological data (eg temperature, humidity, pressure) sourced from NASA.
- **Credits**: Daniel Robert-Nicoud
- **Source**: https://power.larc.nasa.gov/

## Description

|Column|Description|Type|Units|
|-|-|-|-|
|country||str||
|region||str||
|sub_region||str||
|lon|Longitude|float||
|lat|Latitude|float||
|date||pandas.Timestamp||
|avg_temperature|Daily average temperature|float|°C|
|min_temperature|Daily minimal temperature|float|°C|
|max_temperature|Daily maximal temperature|float|°C|
|relative_humidity|Relative humidity (daily<br>average)|float|%|
|specific_humidity|Specific humidity (daily<br>average)|float|kg kg-1|
|pressure|Pressure (daily average)|float|kPa|

## Transformations applied

- No transformations are applied.
- The data is sourced at coordinates provided by the user.
- The specific desired data is sourced through NASA's POWER API.
