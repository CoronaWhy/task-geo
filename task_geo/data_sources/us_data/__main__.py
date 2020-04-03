"""
Main method

Description:
    - Runs us_census which gets the finalized DataFrame for US Census Data
    - Converts and exports to CSV
"""

import us_census


def main():
    us_census().to_csv("us-census-data.csv", header=True)


if __name__ == '__main__':
    main()
