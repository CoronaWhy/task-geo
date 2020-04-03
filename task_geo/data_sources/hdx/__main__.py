from task_geo.data_sources.hdx.hdx_connector import acap_connector
from task_geo.data_sources.hdx.hdx_formatter import acap_formatter


def main():
    raw = acap_connector()
    acap_formatter(raw).to_csv('Goverment Measures Dataset.csv')


if __name__ == '__main__':
    main()
