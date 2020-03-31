from gendiff import parsers


def make_result(source, key, value, status, old_value=None):
    if isinstance(value, dict):
        value = 'complex value'
    if status == 'added':
        source[key] = f"Was added with value: '{value}'"
    elif status == 'deleted':
        source[key] = f"Was removed"
    elif status == 'replaced':
        source[key] = f"Was changed from '{old_value}' to\
 '{value}'"
    elif status == 'unmodified':
        source[key] = f"The value did not change"
    return source


def diff_rendering(items):
    result = {}
    for item in items:
        if items[item][0] == 'nested':
            result[item] = diff_rendering(items[item][1])
        elif items[item][0] == 'replaced':
            make_result(result, item, items[item][1], 'replaced',
                        items[item][2])
        else:
            make_result(result, item, items[item][1], items[item][0])
    return result


def json_formatting(data):
    diff = diff_rendering(data)
    return parsers.json_convert(diff)
