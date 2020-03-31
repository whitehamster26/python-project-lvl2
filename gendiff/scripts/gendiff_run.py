import argparse
from gendiff import gendiff, parsers
from gendiff.formatters import json_like_rendering, plain_text_rendering
from gendiff.formatters import json_rendering


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str, help='select first file \
     to compare')
parser.add_argument('second_file', type=str, help='select second file \
     to compare')
parser.add_argument('-f', '--format', type=str, help='set format of \
    output')


def main():
    args = parser.parse_args()
    file_format = parsers.parse_format(args.first_file)
    first_file_data, second_file_data = \
        parsers.parse_data(file_format, args.first_file, args.second_file)
    diff = gendiff.generate_diff(first_file_data, second_file_data)
    if not args.format:
        print(json_like_rendering.diff_rendering(diff))
    elif args.format == 'plain':
        print(plain_text_rendering.diff_rendering(diff))
    elif args.format == 'json':
        print(json_rendering.json_formatting(diff))
    return None


if __name__ == "__main__":
    main()
