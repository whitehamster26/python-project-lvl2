from gendiff.gendiff import DELETED, ADDED, REPLACED, NESTED


def make_result(key, value, status, replaced_value=None):
    if value is True:
        value = 'true'
    elif isinstance(value, dict):
        value = 'complex value'
    if status == DELETED:
        result = f"Property '{key}' was removed"
    elif status == ADDED:
        result = f"Property '{key}' was added with value: '{value}'"
    elif status == REPLACED:
        result = f"Property '{key}' was changed. From '{replaced_value}' to \
'{value}'"
    return result + '\n'


def render_diff(diff, root_key=None):
    result = ''
    for item in diff.items():
        tree_items = f"{root_key}.{item[0]}" if root_key else item[0]
        if item[1][0] == NESTED:
            result += render_diff(item[1][1], tree_items) + '\n'
        elif item[1][0] == REPLACED:
            result += make_result(tree_items, item[1][1],
                                  REPLACED, item[1][2])
        elif item[1][0] in (ADDED, DELETED):
            result += make_result(tree_items, item[1][1],
                                  item[1][0])
    return result.rstrip('\n')
