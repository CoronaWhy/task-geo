# Government Measures Dataset

## General information

- **Description**: The #COVID19 Government Measures Dataset puts together all the measures implemented by governments worldwide in response to the Coronavirus pandemic. Data collection includes secondary data review.

The researched information available falls into five main categories:
- Social distancing
- Movement restrictions
- Public health measures
- Social and economic measures
- Lockdowns

Each category is broken down into several types of measures.

ACAPS consulted government, media, United Nations, and other organisations sources.
- **Credits**: HDX, ACAPS,
- **Source**: https://data.humdata.org/dataset/acaps-covid19-government-measures-dataset

## Columns in the refined dataset

**COUNTRY**
- Description: Country Name
- Type: Text

**ISO**
- Description: Country in Alpha 3 ISO
- Type: Text

**REGION**
- Description: Region
- Type: Text

**CATEGORY**
- Description: 6 categories in the dataset: Public health measures, Lockdown, Social and economic measures,Social distancing, Movement restrictions, Humanitarian Exemption
- Type: Text

**MEASURE**
- Description: Measures taken by a country or region
    - Additional health/documents requirements upon arrival
    - Amendments to funeral and burial regulations
    - Awareness campaigns
    - Border closure 
    - Border checks
    - Changes in prison-related policies
    - Checkpoints within the country
    - Complete border closure
    - Curfews
    - Domestic travel restrictions
    - Economic measures
    - Emergency administrative structures activated or established
    - Full lockdown
    - General recommendations
    - Health screenings in airports and border crossings
    - Humanitarian exemptions
    - International flights suspension
    - Introduction of quarantine policies
    - Limit product imports/exports
    - Limit public gatherings
    - Lockdown of refugee/idp camps or other minorities
    - Mass population testing
    - Military deployment
    - Obligatory medical tests not related to COVID-19
    - Partial lockdown
    - Psychological assistance and medical social work
    - Public services closure 
    - Schools closure 
    - State of emergency declared
    - Strengthening the public health system
    - Surveillance and monitoring
    - Testing policy
    - Visa restrictions
- Type: Text

**TARGET**
- Description: Need to be determined
- Type: Text

**COMMENT**
- Description: Comments take from source
- Type: Text

**NON_COMPLIANCE**
- Description: Need to be determined
- Type: Text

**DATE_IMPLEMENTED**
- Description: Measure implement on some date dd/mm/yyyy
- Type: Date
- Units: Date

**SOURCE**
- Description: Source
- Type: Text

**SOURCE_TYPE**
- Description: Source types: can be used for reliability
    - Government
    - Media
    - Other
    - Other Organization
    - Social Media
    - Blank
- Type: Text

**ENTRY_DATE**
- Description: The date when this data was added to this dataset
- Type: Date dd/mm/yyyy
- Units: Date

## Transformations applied

- Filtering: Removed columns - 'id', 'pcode', 'admin_level_name', 'link', 'alternative source'

