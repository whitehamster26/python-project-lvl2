import pytest # noqa F401
from gendiff.gendiff import generate_diff


def json_gendiff():
    result_source = open('./gendiff/tests/fixtures/expected_result.txt', 'r')
    test_case = result_source.read()
    assert generate_diff('./gendiff/tests/fixtures/first_file.json', './gendiff/tests/fixtures/second_file.\
json', 'json') == test_case


def yaml_gendiff():
    result_source = open('./gendiff/tests/fixtures/expected_result.txt', 'r')
    test_case = result_source.read()
    assert generate_diff('./gendiff/tests/fixtures/first_file.yml', './gendiff/tests/fixtures/second_file.\
yml', 'yaml') == test_case


def do_tests():
    json_gendiff()
    yaml_gendiff()
