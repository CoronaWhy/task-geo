import pandas as pd


def cds_formatter(df):
    """Formats data from CoronaDataScraper.
    Arguments:
        df(pandas.DataFrame): Raw data returned from cds_connector.

    Returns:
        pandas.DataFrame
    """

    assert df[pd.isnull(df.country)].empty

    df = df.rename(columns={'growthFactor': 'growth_factor'})
    df = df.reindex(columns=[
        'city', 'county', 'state', 'country', 'population', 'lat', 'long',
        'date', 'url', 'aggregate', 'tz', 'cases', 'deaths', 'recovered',
        'active', 'tested', 'growth_factor'
    ])
    df['date'] = pd.to_datetime(df.date)

    return df.sort_values(by='date').reset_index(drop=True)
