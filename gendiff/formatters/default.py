RENDER_SIGNS = {'unmodified': None,
                'added': '+',
                'deleted': '-'}


def make_result(source, key, value, spaces, sign=None):
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
                                 spaces,
                                 sign=None)
        elif items[item][0] in RENDER_SIGNS.keys() and \
                isinstance(items[item][1], dict):
            result = make_result(result, item,
                                 diff_rendering(items[item][1],
                                                spaces=spaces+4),
                                 spaces,
                                 sign=RENDER_SIGNS[items[item][0]])
        elif items[item][0] in RENDER_SIGNS.keys():
            result = make_result(result, item, items[item][1], spaces,
                                 RENDER_SIGNS[items[item][0]])
        elif items[item][0] == 'replaced':
            result = make_result(result, item, items[item][1], spaces, '+')
            result = make_result(result, item, items[item][2], spaces, '-')
    result = result + ((' ' * (spaces-2)) + '}')
    return result
