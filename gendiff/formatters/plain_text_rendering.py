def make_result(source, key, value, status, replaced_value=None):
    if value is True:
        value = 'true'
    elif isinstance(value, dict):
        value = 'complex value'
    if status == 'deleted':
        result = f"Property '{key}' was removed"
    elif status == 'added':
        result = f"Property '{key}' was added with value: '{value}'"
    elif status == 'replaced':
        result = f"Property '{key}' was changed. From '{replaced_value}' to \
'{value}'"
    return source + result + '\n'


def diff_rendering(items, root_key=None):
    result = ''
    for item in items:
        tree_items = f"{root_key}.{item}" if root_key else item
        if items[item][0] == 'nested':
            result += diff_rendering(items[item][1], tree_items) + '\n'
        elif items[item][0] == 'added':
            result = make_result(result, tree_items, items[item][1], 'added')
        elif items[item][0] == 'deleted':
            result = make_result(result, tree_items, items[item][1], 'deleted')
        elif items[item][0] == 'replaced':
            result = make_result(result, tree_items, items[item][1],
                                 'replaced', items[item][2])
    return result.rstrip('\n')
