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
        if isinstance(replaced_value, dict):
            replaced_value = 'complex value'
        result = f"Property '{key}' was changed. From '{replaced_value}' to \
'{value}'"
    return result + '\n'


def render_diff(diff, root_key=None):
    result = ''
    for key, value in diff.items():
        tree_items = f"{root_key}.{key}" if root_key else key
        if value[0] == NESTED:
            result += render_diff(value[1], tree_items) + '\n'
        elif value[0] == REPLACED:
            result += make_result(tree_items, value[1],
                                  REPLACED, value[2])
        elif value[0] in (ADDED, DELETED):
            result += make_result(tree_items, value[1],
                                  value[0])
    return result.rstrip('\n')
