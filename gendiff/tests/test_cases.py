import pytest # noqa F401
from gendiff.gendiff import show_difference


def json_gendiff():
    result_source = open('./gendiff/tests/fixtures/expected_result.txt', 'r')
    test_case = result_source.read()
    diff = show_difference('./gendiff/tests/fixtures/first_file.json', './gendiff/tests/fixtures/second_file.\
json', 'json')
    assert diff == test_case
    result_source = open('./gendiff/tests/fixtures/expected_json_tree.txt',
                         'r')
    test_case = result_source.read()
    diff = show_difference('./gendiff/tests/fixtures/before.json', './gendiff/tests/fixtures/after.\
json', 'json')
    assert diff == test_case


def yaml_gendiff():
    result_source = open('./gendiff/tests/fixtures/expected_result.txt', 'r')
    test_case = result_source.read()
    diff = show_difference('./gendiff/tests/fixtures/first_file.yml', './gendiff/tests/fixtures/second_file.\
yml', 'yaml')
    assert diff == test_case


def do_tests():
    json_gendiff()
    yaml_gendiff()
