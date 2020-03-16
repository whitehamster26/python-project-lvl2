import json


def make_result(source, key, value, sign=None, spaces=2):
    string_spaces = ''
    if not sign:
        sign = ' '
    for _ in range(spaces):
        string_spaces = string_spaces + ' '
    if value is True:
        value = 'true'
    result = f'{string_spaces}{sign} {key}: {value}\n'
    return source + result


def compare_keys(first_file_data, second_file_data):
    def compare_values(first_value, second_value):
        nonlocal result
        if first_value == second_value:
            result = make_result(result, key, first_value)
        else:
            result = make_result(result, key, second_value, '+')
            result = make_result(result, key, first_value, '-')
    result = '{' + '\n'
    for key in first_file_data:
        if key in second_file_data:
            compare_values(first_file_data[key], second_file_data[key])
        elif key not in second_file_data:
            result = make_result(result, key, first_file_data[key], '-')
    for key in second_file_data:
        if key not in first_file_data:
            result = make_result(result, key, second_file_data[key], '+')
    result = result + '}'
    return result


def generate_diff(first_file, second_file, format=None):
    first_file_data = json.load(open(first_file))
    second_file_data = json.load(open(second_file))
    return compare_keys(first_file_data, second_file_data)


def show_difference(first_file, second_file, format=None):
    print(generate_diff(first_file, second_file, format=None))
    return None
