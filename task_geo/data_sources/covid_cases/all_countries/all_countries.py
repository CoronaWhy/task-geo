""" Source of Data: https://coronadatascraper.com/#timeseries.json """

import pandas as pd
import numpy as np
import time


def cds_connector(country):
  """
    Input:  Accept country value in 3 digit format
    Output: Return raw dataframe of all countries
  """
  df = pd.read_csv("https://coronadatascraper.com/timeseries.csv")
  return df[df['country']==country]


def cds_formatter(df):
  """
    Input:  Raw data from Connector 
    Output: Return data frame of the specified country 
  """
  #Check whether any country is missing or not
  assert df[pd.isnull(df.country)].empty
  
  df = df.rename(columns={'growthFactor':'growth_factor'})
  df = df.reindex(columns=['city', 'county', 'state', 'country', 'population', 'lat', 'long', 'date',
       'url', 'aggregate', 'tz', 'cases', 'deaths', 'recovered', 'active',
       'tested', 'growth_factor'])
  
  #Convert column to datetime format from str
  df['date'] = pd.to_datetime(df.date)

  return df.sort_values(by='date').reset_index(drop=True)


def cds_datasource(country):
  '''
    Input:  Accept Country name as 3 digit code
    Output: Return formatted dataframe of all countries
  '''
  data = cds_connector(country)
  return cds_formatter(data)
