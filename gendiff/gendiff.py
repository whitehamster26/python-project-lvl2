from gendiff import parsers


RENDER_SIGNS = {'unmodified': None,
                'added': '+',
                'deleted': '-'}


def generate_diff(first_file_data, second_file_data):
    diff = {}
    for key in first_file_data:
        if key in second_file_data:
            if first_file_data[key] == second_file_data[key]:
                diff[key] = ('unmodified', first_file_data[key])
            else:
                if isinstance(first_file_data[key], dict) and \
                        isinstance(second_file_data[key], dict):
                    diff[key] = ('nested', generate_diff(
                        first_file_data[key], second_file_data[key]))
                else:
                    diff[key] = ('replaced', second_file_data[key],
                                 first_file_data[key])
        elif key not in second_file_data:
            if isinstance(first_file_data[key], dict):
                diff[key] = ('deleted', generate_diff(
                    first_file_data[key],
                    first_file_data[key]))
            else:
                diff[key] = ('deleted', first_file_data[key])
    for key in second_file_data:
        if key not in first_file_data:
            if isinstance(second_file_data[key], dict):
                diff[key] = ('added', generate_diff(
                    second_file_data[key],
                    second_file_data[key]))
            else:
                diff[key] = ('added', second_file_data[key])
    return diff


def make_result(source, key, value, sign=None, spaces=2):
    string_spaces = '' + (' ' * spaces)
    if not sign:
        sign = ' '
    if value is True:
        value = 'true'
    result = f'{string_spaces}{sign} {key}: {value}\n'
    return source + result


def diff_rendering(items, spaces=2):
    result = ((' ' * (spaces-spaces)) + '{' + '\n')
    for item in items:
        if items[item][0] == 'nested':
            result = make_result(result, item,
                                 diff_rendering(items[item][1],
                                                spaces=spaces+4),
                                 sign=None,
                                 spaces=spaces)
        elif items[item][0] in RENDER_SIGNS.keys() and \
                isinstance(items[item][1], dict):
            result = make_result(result, item,
                                 diff_rendering(items[item][1],
                                                spaces=spaces+4),
                                 sign=RENDER_SIGNS[items[item][0]],
                                 spaces=spaces)
            # нужно пофиксить, знаки не отображаются в рендере ^
        elif items[item][0] == 'added':
            result = make_result(result, item, items[item][1], '+',
                                 spaces=spaces)
        elif items[item][0] == 'deleted':
            result = make_result(result, item, items[item][1], '-',
                                 spaces=spaces)
        elif items[item][0] == 'unmodified':
            result = make_result(result, item, items[item][1],
                                 sign=None, spaces=spaces)
        elif items[item][0] == 'replaced':
            result = make_result(result, item, items[item][1], '+',
                                 spaces=spaces)
            result = make_result(result, item, items[item][2], '-',
                                 spaces=spaces)
    result = result + ((' ' * (spaces-2)) + '}')
    return result


def show_difference(first_file, second_file, format=None):
    if not format:
        format = parsers.parse_format(first_file)
    first_file_data, second_file_data = \
        parsers.parse_data(format, first_file, second_file)
    diff = generate_diff(first_file_data, second_file_data)
    print(diff_rendering(diff))
    return diff_rendering(diff)
