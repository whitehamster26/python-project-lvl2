from gendiff import parsers


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


def generate_diff(first_file, second_file, format=None):
    first_file_data, second_file_data =\
         parsers.parse_data(format, first_file, second_file)
    result = '{' + '\n'
    for key in first_file_data:
        if key in second_file_data:
            if first_file_data[key] == second_file_data[key]:
                result = make_result(result, key, first_file_data[key])
            else:
                result = make_result(result, key, second_file_data[key], '+')
                result = make_result(result, key, first_file_data[key], '-')
        elif key not in second_file_data:
            result = make_result(result, key, first_file_data[key], '-')
    for key in second_file_data:
        if key not in first_file_data:
            result = make_result(result, key, second_file_data[key], '+')
    result = result + '}'
    return result


def show_difference(first_file, second_file, format=None):
    if not format:
        format = parsers.parse_format(first_file)
    print(generate_diff(first_file, second_file, format))
    return None
