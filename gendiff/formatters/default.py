from gendiff.gendiff import UNMODIFIED, DELETED, ADDED, REPLACED, NESTED

RENDER_SIGNS = {UNMODIFIED: None,
                ADDED: '+',
                DELETED: '-',
                NESTED: None}


def make_result(key, value, spaces, sign=None):
    string_spaces = '' + (' ' * spaces)
    if not sign:
        sign = ' '
    if value is True:
        value = 'true'
    result = f'{string_spaces}{sign} {key}: {value}\n'
    return result


def render_diff(diff, spaces=2):
    result = '{' + '\n'
    for item in diff.items():
        if item[1][0] == NESTED:
            result += make_result(item[0],
                                  render_diff(item[1][1],
                                  spaces=spaces+4),
                                  spaces)
        elif isinstance(item[1][1], dict):
            result += make_result(item[0],
                                  render_diff(item[1][1], spaces=spaces+4),
                                  spaces, sign=RENDER_SIGNS[item[1][0]])
        elif item[1][0] == REPLACED:
            # need to build a new tree if any key has objects
            result += make_result(item[0], item[1][1], spaces=spaces, sign='+')
            result += make_result(item[0], item[1][2], spaces=spaces, sign='-')
        else:
            result += make_result(item[0], item[1][1], spaces=spaces,
                                  sign=RENDER_SIGNS[item[1][0]])
    result += ' ' * (spaces-2) + '}'
    return result
