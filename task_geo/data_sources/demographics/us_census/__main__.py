"""
Main method

Description:
    - Runs us_census which gets the finalized DataFrame for US Census Data
    - Converts and exports to CSV
"""

from task_geo.data_sources.demographics.us_census import us_census


def main():
    us_census().to_csv("us-census-data.csv", header=True)


if __name__ == '__main__':
    main()
