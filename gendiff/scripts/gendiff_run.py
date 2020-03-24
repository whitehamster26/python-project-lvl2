import argparse
from gendiff import gendiff


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str, help='select first file \
     to compare')
parser.add_argument('second_file', type=str, help='select second file \
     to compare')
parser.add_argument('-f', '--format', type=str, help='set format of \
    output')


def main():
    args = parser.parse_args()
    gendiff.show_difference(args.first_file, args.second_file, args.format)
    return None


if __name__ == "__main__":
    main()
