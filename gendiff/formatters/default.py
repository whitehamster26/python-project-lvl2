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
    for key, value in diff.items():
        if value[0] == NESTED:
            result += make_result(key,
                                  render_diff(value[1], spaces=spaces+4),
                                  spaces)
        elif isinstance(value[1], dict) and not value[0] == REPLACED:
            result += make_result(key,
                                  render_diff(value[1], spaces=spaces+4),
                                  spaces, sign=RENDER_SIGNS[value[0]])
        elif value[0] == REPLACED:
            if isinstance(value[1], dict) and not isinstance(value[2], dict):
                result += make_result(key, render_diff(value[1],
                                                       spaces=spaces+4),
                                      spaces=spaces, sign='+')
                result += make_result(key, value[2], spaces=spaces, sign='-')
            elif not isinstance(value[1], dict) and isinstance(value[2], dict):
                result += make_result(key, value[1], spaces=spaces, sign='+')
                result += make_result(key, render_diff(value[2],
                                                       spaces=spaces+4),
                                      spaces=spaces, sign='-')
            else:
                result += make_result(key, value[1], spaces=spaces, sign='+')
                result += make_result(key, value[2], spaces=spaces, sign='-')
        else:
            result += make_result(key, value[1], spaces=spaces,
                                  sign=RENDER_SIGNS[value[0]])
    result += ' ' * (spaces-2) + '}'
    return result
