import pandas as pd

MOBILITY_REPORTS_URL = 'https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv'


def mobility_connector():
    """Retrieves the Google mobility report."""
    return pd.read_csv(MOBILITY_REPORTS_URL)
