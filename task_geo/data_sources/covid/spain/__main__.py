from task_geo.data_sources.covid.spain import es_covid_connector, es_covid_formatter


def main():
    data = es_covid_connector()
    es_covid_formatter(data).to_csv("data.csv", index=False)


if __name__ == '__main__':
    main()
