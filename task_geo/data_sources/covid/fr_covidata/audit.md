# COVID-19 Granular Data - France

## General information

- **Description**: COVID-19 daily confirmed cases/hospitalized/recovering/recovered/deaths data in different subregions of France
- **Credits**: @opencovid19-fr
- **Source**: https://github.com/opencovid19-fr/data/

## Column Details

**subregion_code**
- Description: French Maille department code
- Type: str

**subregion_name**
- Description: French department name
- Type: str

**country**
- Description: Country Name - France
- Type: str

**date**
- Description: yyyy/mm/dd Date
- Type: datetime.date

**confirmed**
- Description: Cumulative number of confirmed covid-19 cases at the given location until the given time
- Type: float

**hospitalized**
- Description: Number of hospitalized people due to covid-19 at the given location at the given time
- Type: float

**recovering**
- Description: Number of people recovering from covid-19 at the given location at the given time
- Type: float

**recovered**
- Description: Cumulative number of people healed from covid-19 at the given location until the given time
- Type: float

**deaths**
- Description: Cumulative number of people who passed away from covid-19 at the given location until the given time
- Type: float

**source_name**
- Description: Name of the source of information relevant to the given location at the given time
- Type: str

**source_url**
- Description: Uniform Resource Locator link of the source of information relevant to the given location at the given time
- Type: str

**source_name**
- Description: Uniform Resource Locator link of the archive of the source of information relevant to the given location at the given time
- Type: str

**source_name**
- Description: Type of the source of information: National Health Ministry/Regional health agencies
- Type: str

## Transformations applied

- Deleting the rows non-related to the departments inside Metropolitan France ('region', 'monde', 'pays', 'collectivite-outremer', 'DEP-971', 'DEP-972', 'DEP-973', 'DEP-974', 'DEP-976')
- Dropping the columns 'depistes' and 'granularite'
- Deleting the dupicate rows containing the same numerical data
- Switching the 'date' column format from str to datetime.date
- Switching the 'source_nom', 'source_url', 'source_archive', 'source_type'' columns format to str
- Merging all the rows that have the same 'date' and 'subregion_name' column value, by taking the maximum of every numerical column value and aggregating both sources columns' info
- Renaming/Translating the column titles from French to English, and rearranging them
