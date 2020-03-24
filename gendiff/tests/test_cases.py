import pytest # noqa F401
from gendiff.gendiff import generate_diff


def first_test_case():
    result_source = open('./gendiff/tests/fixtures/expected_result.txt', 'r')
    test_case = result_source.read()
    assert generate_diff('./gendiff/tests/fixtures/first_file.json', './gendiff/tests/fixtures/second_file.\
json') == test_case


def do_tests():
    first_test_case()
