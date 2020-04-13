from gendiff import parsers


def test_parse_data():
    test_cases = [('./tests/fixtures/second_file.json', '.json'),
                  ('./tests/fixtures/second_file.yml', '.yml')]
    for case in test_cases:
        assert type(parsers.parse_data(case[1], case[0])) == dict
