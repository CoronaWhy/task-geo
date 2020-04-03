Data model
----------

This is a reference for the data model of the different data we are gathering:

Altough there are no rules on which language or framework to use, I will write in the case of Python and Pandas, in case of somebody working with another language (like R or Java), most of this rules are easy to translate, in case of doubt, please feel free to discuss in #task-geo.


General guidelines
==================

- Cite the source of your data. ( In the docstring of your data_source file, and on the
  ``AUTHORS.rst`` Data Sources section and, of course, include yourself among the contributors).

- Units should be in metric system, codes like country codes, should be ISO.

- Column names should be lowercase (it might be uglier, but it's easier when coding).

- Unless strictly necessary, we should try avoid having multiindices.

- Avoid making totalizations of data, the more granular data, the best, we can always aggregate,
  but we can't disaggregate.

- Avoid unecessary stacking of data:

  Don't do this:

    +----------+-------+-----+
    | date     |measure|value|
    +----------+-------+-----+
    |2020-01-01| A     | 1.5 |
    +----------+-------+-----+
    |2020-01-01| B     | 2.0 |
    +----------+-------+-----+
    |2020-01-02| A     | 1.0 |
    +----------+-------+-----+
    |2020-01-02| B     | 0.5 |
    +----------+-------+-----+

  Do this instead:

    +----------+-------+-----+
    |date      | A     |  B  |
    +----------+-------+-----+
    |2020-01-01| 1.5   | 2.0 |
    +----------+-------+-----+
    |2020-01-02| 1.0   | 0.5 |
    +----------+-------+-----+

   **THIS DOESN'T APPLY TO TIME DATA!!!**

- Avoid unnecesary flattening/unstacking of data: (Yes, it may seem contradictory with the last
  point but it's not!)

  This may come in hand when working with one-hot encoded variables or unstructured or schemaless
  data using dataframes, for example, for the following JSON:

  .. code-block:: python

    [
        {
            'id': 2,
            'feature_A': 0.1,
            'feature_B': 1.4,
            'feature_C': 1.5,
        },
        {
            'id': 1,
            'feature_X': 14.5,
            'feature_Y': 2.0,
            'feature_Z': 41
        }
    ]


  Don't do this:
  
  +----+-----------+-----------+-----------+-----------+-----------+-----------+
  | id | feature_A | feature_B | feature_C | feature_X | feature_Y | feature_Z |
  +----+-----------+-----------+-----------+-----------+-----------+-----------+
  | 1  | 0.1       |  1.4      |  1.5      | nan       | nan       | nan       |
  +----+-----------+-----------+-----------+-----------+-----------+-----------+
  | 2  | nan       | nan       | nan       | 14.5      | 2.0       | 41        |
  +----+-----------+-----------+-----------+-----------+-----------+-----------+

  Do this instead:

  +----+---------+-------+
  | id | feature | value |
  +----+---------+-------+
  | 1  | A       | 0.1   |
  +----+---------+-------+
  | 1  | B       | 1.4   |
  +----+---------+-------+
  | 1  | C       | 1.5   |
  +----+---------+-------+
  | 2  | X       | 14.5  |
  +----+---------+-------+
  | 2  | Y       | 2.0   |
  +----+---------+-------+
  | 2  | Z       | 41    |
  +----+---------+-------+

  It's hard to define an explicit set of rules, but I'll say:

  1. Try to avoid adding NaN to your data because of the shaping.
  2. Try to make your date the most compact possible
  3. In case of doubt, please, don't hesistate to ask on Slack #team-geo!


Geographical data
=================

- Columns with geographical-related information should be at the beginning of the dataset.

- Latitude and longitude should be in decimal values, not in degrees.

- Enrich your location (lat, long) data with the geopolitical information(city, country) when possible.
  You can use something like https://opencagedata.com/

- Columns containing ISO codes instead of names, should append `_iso` at the end of the name.

- In case political subdivisions are available, each subdivision should be in its own column,
  those columns should be: ``country``, ``region``, ``subregion`` ``city``. If information after some
  level is not available the column is not required.


Time-related data
=================

- If we have have columns for time-related data, they should be after the geographical columns
  of the dataframe.

- The column containing the date should be of `dtype` `datetime`, that is: no date as string or
  int(something like ``20200328`` instead of ``2020/03/28``).

- Avoid using full timestamps (date + time) if your data doesn't provide time information, will
  avoid unnecessary noise. ( don't use ``2020-03-28T00:00:00``, instead use ``2020/03/28``, altough
  pandas does that for you automatically most of the time)