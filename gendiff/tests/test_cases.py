import pytest # noqa F401
from gendiff import gendiff, parsers
from gendiff.formatters import json_like_rendering, plain_text_rendering


def json_gendiff():
    result_source = open('./gendiff/tests/fixtures/expected_result.txt', 'r')
    test_case = result_source.read()
    first_file_data, second_file_data = parsers.json_parse('./gendiff\
/tests/fixtures/first_file.json', './gendiff/tests/fixtures/second_file.json')
    diff = gendiff.generate_diff(first_file_data, second_file_data)
    assert json_like_rendering.diff_rendering(diff) == test_case
    result_source = open('./gendiff/tests/fixtures/expected_json_tree.txt',
                         'r')
    test_case = result_source.read()
    first_file_data, second_file_data = parsers.json_parse('./gendiff\
/tests/fixtures/before.json', './gendiff/tests/fixtures/after.json')
    diff = gendiff.generate_diff(first_file_data, second_file_data)
    assert json_like_rendering.diff_rendering(diff) == test_case


def yaml_gendiff():
    result_source = open('./gendiff/tests/fixtures/expected_result.txt', 'r')
    test_case = result_source.read()
    first_file_data, second_file_data = parsers.yaml_parse('./gendiff\
/tests/fixtures/first_file.yml', './gendiff/tests/fixtures/second_file.yml')
    diff = gendiff.generate_diff(first_file_data, second_file_data)
    assert json_like_rendering.diff_rendering(diff) == test_case


def plain_test():
    result_source = open('./gendiff/tests/fixtures/expected_plain.txt', 'r')
    test_case = result_source.read()
    first_file_data, second_file_data = parsers.json_parse('./gendiff\
/tests/fixtures/before.json', './gendiff/tests/fixtures/after.json')
    diff = gendiff.generate_diff(first_file_data, second_file_data)
    assert plain_text_rendering.diff_rendering(diff) == test_case


def do_tests():
    json_gendiff()
    yaml_gendiff()
    plain_test()
