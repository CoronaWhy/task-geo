from task_geo.data_sources.mobility.mobility_connector import mobility_connector
from task_geo.data_sources.mobility.mobility_formatter import mobility_formatter


def mobility(download_folder, download=True, skip_downloaded=True):
    """Process the mobility reports from Google.

    The behavior with the download parameters is the following:

    - If download is and skip_downloaded are both ``True``(default behavior):
        It will download the files, the first time is executed, and skip it the following times.

    - If download is ``True`` and ``skip_download`` is False:
        It will download the files every execution.

    - If download is ``False``:
        The files will not be downloaded, and the connector and formatter
    will try to find the files in ``download_folder``


    Arguments:
        download_folder(str):
            Path to the folder where pdf will be downloaded, will create it if it doesn't exist.
        download(bool): Wheter or not to download download the reports.
        skip_downloaded(bool): Wheter or not skip downloaded files.

    Returns:
        pandas.DataFrame

    """
    raw = mobility_connector(download_folder, download, skip_downloaded)
    return mobility_formatter(raw)
