from gendiff import gendiff, parsers, formatters

PATH = './tests/fixtures/'


def test_default_plain():
    with open(f'{PATH}expected_result.txt', 'r') as f:
        expected_result = f.read()
        first_file = parsers.get_data(f'{PATH}first_file.yml')
        second_file = parsers.get_data(f'{PATH}second_file.yml')
        diff = gendiff.build_diff(first_file, second_file)
        assert formatters.default(diff) == expected_result
        first_file = parsers.get_data(f'{PATH}first_file.json')
        second_file = parsers.get_data(f'{PATH}second_file.json')
        diff = gendiff.build_diff(first_file, second_file)
        assert formatters.default(diff) == expected_result


def test_tree():
    with open(f'{PATH}expected_json_tree.txt', 'r') as f:
        expected_result = f.read()
        first_file = parsers.get_data(f'{PATH}before.json')
        second_file = parsers.get_data(f'{PATH}after.json')
        diff = gendiff.build_diff(first_file, second_file)
        assert formatters.default(diff) == expected_result


def test_plain():
    with open(f'{PATH}expected_plain.txt', 'r') as f:
        expected_result = f.read()
        first_file = parsers.get_data(f'{PATH}before.json')
        second_file = parsers.get_data(f'{PATH}after.json')
        diff = gendiff.build_diff(first_file, second_file)
        assert formatters.plain(diff) == expected_result


def test_json():
    with open(f'{PATH}expected_result.json', 'r') as f:
        expected_result = f.read()
        first_file = parsers.get_data(f'{PATH}before.json')
        second_file = parsers.get_data(f'{PATH}after.json')
        diff = gendiff.build_diff(first_file, second_file)
        assert formatters.json(diff) == expected_result
