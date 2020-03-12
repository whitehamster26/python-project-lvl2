import argparse
parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str, help='select first file \
     to compare')
parser.add_argument('second_file', type=str, help='select second file \
     to compare')
parser.add_argument('-f', '--format', type=str, help='set format of \
    output')


def main():
    args = parser.parse_args()  # noqa: F841


if __name__ == "__main__":
    main()
