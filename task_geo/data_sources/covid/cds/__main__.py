from task_geo.data_sources.covid.cds import cds_connector, cds_formatter


def main():
    data = cds_connector()
    cds_formatter(data).to_csv("data.csv")


if __name__ == '__main__':
    main()
