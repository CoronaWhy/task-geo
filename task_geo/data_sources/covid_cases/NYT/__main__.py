import argparse

from nyt import us_covid_nyt


def get_argparser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-o', '--output', required=True,
        help='Destination file to store the processed dataset.')

    return parser


def main():
    parser = get_argparser()
    args = parser.parse_args()

    dataset = us_covid_nyt()
    dataset.to_csv(args.output, index=False, header=True)


if __name__ == '__main__':
    main()
