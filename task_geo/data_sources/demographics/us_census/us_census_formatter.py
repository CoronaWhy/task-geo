def us_census_formatter(data):
    """Formatter for US Census.

    Arguments:
        data(pandas.DataFrame): Data as returned by us_census_connector.

    Description:
        - Drop unnecessary columns and set index to county
        - Make column values more readable

    Returns:
        pandas.DataFrame
    """

    data.columns = data.iloc[0]
    data.drop(0, inplace=True)
    data.drop("id", axis=1, inplace=True)
    data = data.set_index('Geographic Area Name')

    cols = [c for c in data.columns if '2018' in c]
    data = data[cols]
    data.columns = [x.split("!!")[-1] for x in data.columns]

    data = data.replace("N", 0.0)
    data.columns = [x.lower() for x in data.columns]

    data.drop(data.columns[-1], axis=1, inplace=True)
    data.drop(data.columns[-1], axis=1, inplace=True)

    return data
