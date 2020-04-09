import pandas as pd


def cds_formatter(df):
    """Formats data from CoronaDataScraper.
    Arguments:
        df(pandas.DataFrame): Raw data returned from cds_connector.

    Returns:
        pandas.DataFrame
    """

    assert df[pd.isnull(df.country)].empty

    del df['population']
    df = df.rename(columns={
        'growthFactor': 'growth_factor',
        'state': 'region',
        'county': 'sub_region'
    })
    df = df.reindex(columns=[
        'country', 'region', 'sub_region', 'city', 'lat', 'long',
        'date', 'url', 'aggregate', 'tz', 'cases', 'deaths', 'recovered',
        'active', 'tested', 'growth_factor'
    ])
    df['date'] = pd.to_datetime(df.date)

    metrics = ['cases', 'deaths', 'recovered', 'active', 'tested']
    df[metrics] = df[metrics].fillna(0).astype(int)
    df.loc[(df["aggregate"] == "state") & (df["region"].isnull()), "aggregate"] = "country"

    return df.sort_values(by='date').reset_index(drop=True)
