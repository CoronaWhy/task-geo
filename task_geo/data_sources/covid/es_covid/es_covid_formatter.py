import pandas as pd


def es_covid_formatter(df):
    """Format data retrieved from https://covid19.isciii.es.

    Arguments:
        raw(pandas.DataFrame):

    Returns:
        pandas.DataFrame

    """
    df.columns = df.columns.str.lower()
    df.rename(columns={'ccaa': 'autonomous_community_iso', 'fecha': 'date',
                       'casos': 'cases', 'hospitalizados': 'hospitalized', 'uci': 'icu',
                       'fallecidos': 'deceased', 'recuperados': 'recovered'}, inplace=True)

    # ### Replace NaN with 0
    df['cases'].fillna(value=0, inplace=True)
    df['hospitalized'].fillna(value=0, inplace=True)
    df['icu'].fillna(value=0, inplace=True)
    df['deceased'].fillna(value=0, inplace=True)
    df['recovered'].fillna(value=0, inplace=True)

    df['date'] = pd.to_datetime(df['date'])

    # Undo cumulative sums
    # create a copy of the dataframe, without date
    unrolled_df = df.copy()
    unrolled_df.drop(['date'], axis=1, inplace=True)

    # unroll (i.e. undo the cumulative values)
    unrolled_df = unrolled_df.groupby('autonomous_community_iso').diff().fillna(unrolled_df)

    # add back autonomous_community_iso, date columns
    unrolled_df = pd.concat([df[['autonomous_community_iso', 'date']], unrolled_df], axis=1)

    # Insert Country
    unrolled_df.insert(0, 'country', 'Spain')

    # Remove rows that are not a region. This is significant because the last row includes
    # some text
    unrolled_df = unrolled_df[unrolled_df['autonomous_community_iso'].isin(
        ["CE", "AR", "CM", "PV", "MC", "AS", "AN", "CL", "CT", "MD", "IB", "GA", "CN", "VC", "RI",
         "NC", "EX", "ME", "CB"])]

    # Add Area, Population, Density, GDP
    unrolled_df['area_km_squared'] = unrolled_df['autonomous_community_iso'].map({"CE": 18.5,
                                                                                  "AR": 47719,
                                                                                  "CM": 79463,
                                                                                  "PV": 7234,
                                                                                  "MC": 11313,
                                                                                  "AS": 10604,
                                                                                  "AN": 87268,
                                                                                  "CL": 94223,
                                                                                  "CT": 32114,
                                                                                  "MD": 8028,
                                                                                  "IB": 4992,
                                                                                  "GA": 29574,
                                                                                  "CN": 7447,
                                                                                  "VC": 23255,
                                                                                  "RI": 5045,
                                                                                  "NC": 10391,
                                                                                  "EX": 41634,
                                                                                  "ME": 12.3,
                                                                                  "CB": 5321
                                                                                  })
    unrolled_df['population'] = unrolled_df['autonomous_community_iso'].map({"CE": 84777,
                                                                             "AR": 1319291,
                                                                             "CM": 2032863,
                                                                             "PV": 2207776,
                                                                             "MC": 1493898,
                                                                             "AS": 1022800,
                                                                             "AN": 8414240,
                                                                             "CL": 2399548,
                                                                             "CT": 7675217,
                                                                             "MD": 6663394,
                                                                             "IB": 1149460,
                                                                             "GA": 2699499,
                                                                             "CN": 2153389,
                                                                             "VC": 5003769,
                                                                             "RI": 316798,
                                                                             "NC": 654214,
                                                                             "EX": 1067710,
                                                                             "ME": 86487,
                                                                             "CB": 581078
                                                                             })
    unrolled_df['density_pop_per_km_squared'] = unrolled_df['population'] / unrolled_df[
        'area_km_squared']

    unrolled_df['gdp_per_capita_euros'] = unrolled_df['autonomous_community_iso'].map({"CE": 19335,
                                                                                       "AR": 25540,
                                                                                       "CM": 17698,
                                                                                       "PV": 30829,
                                                                                       "MC": 18520,
                                                                                       "AS": 21035,
                                                                                       "AN": 16960,
                                                                                       "CL": 22289,
                                                                                       "CT": 27248,
                                                                                       "MD": 29385,
                                                                                       "IB": 24393,
                                                                                       "GA": 20723,
                                                                                       "CN": 19568,
                                                                                       "VC": 19964,
                                                                                       "RI": 25508,
                                                                                       "NC": 29071,
                                                                                       "EX": 15394,
                                                                                       "ME": 16981,
                                                                                       "CB": 22341
                                                                                       })
    # Reorder Columns
    return unrolled_df[
        ['country', 'autonomous_community_iso', 'area_km_squared', 'population',
         'gdp_per_capita_euros', 'density_pop_per_km_squared', 'date', 'cases', 'hospitalized',
         'icu', 'deceased', 'recovered']]
