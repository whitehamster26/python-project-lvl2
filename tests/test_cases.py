import pytest # noqa F401
from gendiff import gendiff, parsers
from gendiff.formatters import json_like_rendering, plain_text_rendering
from gendiff.formatters import json_rendering


def test_json_gendiff():
    result_source = open('./tests/fixtures/expected_result.txt', 'r')
    test_case = result_source.read()
    first_file_data, second_file_data = parsers.json_parse('.\
/tests/fixtures/first_file.json', './tests/fixtures/second_file.json')
    diff = gendiff.generate_diff(first_file_data, second_file_data)
    assert json_like_rendering.diff_rendering(diff) == test_case
    result_source = open('./tests/fixtures/expected_json_tree.txt',
                         'r')
    test_case = result_source.read()
    first_file_data, second_file_data = parsers.json_parse('.\
/tests/fixtures/before.json', './tests/fixtures/after.json')
    diff = gendiff.generate_diff(first_file_data, second_file_data)
    assert json_like_rendering.diff_rendering(diff) == test_case


def test_yaml_gendiff():
    result_source = open('./tests/fixtures/expected_result.txt', 'r')
    test_case = result_source.read()
    first_file_data, second_file_data = parsers.yaml_parse('.\
/tests/fixtures/first_file.yml', './tests/fixtures/second_file.yml')
    diff = gendiff.generate_diff(first_file_data, second_file_data)
    assert json_like_rendering.diff_rendering(diff) == test_case


def test_plain():
    result_source = open('./tests/fixtures/expected_plain.txt', 'r')
    test_case = result_source.read()
    first_file_data, second_file_data = parsers.json_parse('.\
/tests/fixtures/before.json', './tests/fixtures/after.json')
    diff = gendiff.generate_diff(first_file_data, second_file_data)
    assert plain_text_rendering.diff_rendering(diff) == test_case


def test_json():
    result_source = open('./tests/fixtures/expected_json_format.json',
                         'r')
    test_case = result_source.read()
    first_file_data, second_file_data = parsers.json_parse('.\
/tests/fixtures/before.json', './tests/fixtures/after.json')
    diff = gendiff.generate_diff(first_file_data, second_file_data)
    assert json_rendering.json_formatting(diff) == test_case
