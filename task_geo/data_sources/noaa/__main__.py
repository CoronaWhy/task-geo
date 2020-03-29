import argparse

from ftp import download_noaa_files, process_noaa_data


def get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--download',
        action='store_true', help="Wheter download or not the files.")

    parser.add_argument(
        '-o', '--output', required=True,
        help='Destination file to store the processed dataset.')

    parser.add_argument(
        '-c', '--countries', required=True,
        nargs='?', help='FIPS Country codes to select data for.')

    return parser


def main():
    parser = get_argparser()
    args = parser.parse_args()
    if args.download:
        download_noaa_files()
    else:
        dataset = process_noaa_data(args.countries)
        dataset.to_csv(args.output, index=False, header=True)


if __name__ == '__main__':
    main()
