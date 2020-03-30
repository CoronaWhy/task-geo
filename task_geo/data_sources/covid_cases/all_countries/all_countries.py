import pandas as pd
import numpy as np
import time


def all_country_datasource_connector(*args, **kwargs):
  '''
    Input:  None
    Output: Return raw dataframe of all countries
  '''
  df = pd.read_csv("https://coronadatascraper.com/timeseries.csv")
  
  return df

def all_country_datasource_formatter(df):
  '''
    Input:  Raw data from connector method
    Output: Return list of dataframe of all countries
  '''

  df_list = []

  #Remove rows where country is not provided
  df = df[df['country'].notna()]
  #df = df[df['state'].notna()]

  #Get all country list present in dataset

  country_list = df.country.unique()


  #Currently all Country are having null state data values. 
  #Below code will extract Geo-Data as country wise and then save it.

  for country in country_list:
    
    idx = 0

    #Create empty dataframe for storing Country-wise data from main dataframe
    fnl = pd.DataFrame(columns=['state','country','population','lat','long','url','aggregate','tz','date','cases','deaths','recovered','active','growthFactor'])

    ed = df[df['country']==country].sort_values(by='date')

    #Store values ony by one for each country sorted by date
    for date in ed.date.unique():
      fnl.loc[idx] = pd.Series()
      fnl.loc[idx]['state'] = ed[ed['date']==date]['state'].values[0]
      fnl.loc[idx]['country'] = ed[ed['date']==date]['country'].values[0]
      fnl.loc[idx]['population'] = ed[ed['date']==date]['population'].values[0]
      fnl.loc[idx]['lat'] = ed[ed['date']==date]['lat'].values[0]
      fnl.loc[idx]['long'] = ed[ed['date']==date]['long'].values[0]
      fnl.loc[idx]['url'] = ed[ed['date']==date]['url'].values[0]
      fnl.loc[idx]['aggregate'] = ed[ed['date']==date]['aggregate'].values[0]
      fnl.loc[idx]['tz'] = ed[ed['date']==date]['tz'].values[0]
      fnl.loc[idx]['date'] = date
      fnl.loc[idx]['cases'] = ed[ed['date']==date]['cases'].values[0]
      fnl.loc[idx]['deaths'] = ed[ed['date']==date]['deaths'].values[0]
      fnl.loc[idx]['recovered'] = ed[ed['date']==date]['recovered'].values[0]
      fnl.loc[idx]['active'] = ed[ed['date']==date]['active'].values[0]
      fnl.loc[idx]['growthFactor'] = ed[ed['date']==date]['growthFactor'].values[0]
      idx += 1

    df_list.append(fnl)

  return df_list



def all_country_datasource():
  '''
    Input:  None
    Output: Return formatted dataframe of all countries
  '''
  data = all_country_datasource_connector()
  return all_country_datasource_formatter(data)



