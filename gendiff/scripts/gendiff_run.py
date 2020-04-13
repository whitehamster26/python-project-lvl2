import argparse
from gendiff import gendiff, parsers, formatters


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str, help='select first file \
     to compare')
parser.add_argument('second_file', type=str, help='select second file \
     to compare')
parser.add_argument('-f', '--format', type=str, help='set format of \
    output')


def main():
    args = parser.parse_args()
    format_diff = None
    if args.format == formatters.JSON:
        format_diff = formatters.json
    elif args.format == formatters.PLAIN:
        format_diff = formatters.plain
    elif not args.format:
        format_diff = formatters.default
    else:
        raise Exception('Format is not supported.')
    first_file_data = parsers.get_data(args.first_file)
    second_file_data = parsers.get_data(args.second_file)
    diff = gendiff.generate_diff(first_file_data, second_file_data)
    print(format_diff(diff))


if __name__ == "__main__":
    main()
