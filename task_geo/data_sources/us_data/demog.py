import urllib.request
import pandas as pd
import zipfile

url = 'https://data.census.gov/api/access/table/download?download_id=iuGrLXEBm-bIwvlxENnx'

'''
download_us_data method - Gets CSV from URL
	Returns: Pandas DataFrame
'''
def download_us_data():

	urllib.request.urlretrieve(url, "uscensus.zip")
	
	with zipfile.ZipFile("uscensus.zip") as myzip:
	
		# Get list of files in zip file
		listFiles = myzip.namelist()
		
		# Using ACS 5Y Statistics
		myzip.extract(listFiles[5])
		data = pd.read_csv(listFiles[5], low_memory = False)
	
	return data

'''
process_us_data method - Process DataFrame
	Returns: Cleaned Pandas DataFrame
'''
def process_us_data(data):
	
	# Drop unnecessary columns and set index to county
	data.columns = data.iloc[0]
	data.drop(0, inplace=True)
	data.drop("id", axis=1, inplace=True)
	data = data.set_index('Geographic Area Name')
	
	# Make columns readable
	cols = [c for c in data.columns if '2018' in c]
	data = data[cols]
	data.columns = [x.split("!!")[-1] for x in data.columns]
	
	# Lowercase columns
	data = data.replace("N", 0.0)
	data.columns = [x.lower() for x in data.columns]
	return data
	
