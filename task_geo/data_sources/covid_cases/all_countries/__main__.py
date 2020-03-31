from task_geo.data_sources.covid_cases.all_countries import cds_connector
from task_geo.data_sources.covid_cases.all_countries import cds_formatter


def main():
    data = cds_connector("ITA")
    cds_formatter(data).to_csv("data.csv")


if __name__ == '__main__':
    main()
