from demog import download_us_data, process_us_data

def main():
	df = download_us_data()
	new_df = process_us_data(df)
	new_df.to_csv("us-census-data.csv", header=True)
	
if __name__ == '__main__':
	main()