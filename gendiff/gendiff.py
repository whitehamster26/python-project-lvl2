KEYS_STATUS = (UNMODIFIED, DELETED, ADDED, REPLACED, NESTED) = (
    'unmodified', 'deleted', 'added', 'replaced', 'nested'
)


def build_tree(data):
    result = {}
    for key in data:
        if isinstance(data[key], dict):
            result[key] = (NESTED, build_tree(data[key]))
        else:
            result[key] = (UNMODIFIED, data[key])
    return result


def safe_put(status, value, second_value=None):
    if second_value:
        if isinstance(value, dict) and not isinstance(second_value, dict):
            return status, build_tree(value), second_value
        elif not isinstance(value, dict) and isinstance(second_value, dict):
            return status, value, build_tree(second_value)
        else:
            return status, value, second_value
    if isinstance(value, dict):
        return status, build_tree(value)
    else:
        return status, value


def build_status(first_dict, second_dict):
    result = {}
    result[UNMODIFIED] = first_dict.keys() & second_dict.keys()
    result[DELETED] = first_dict.keys() - second_dict.keys()
    result[ADDED] = second_dict.keys() - first_dict.keys()
    return result


def build_diff(primary_data, modified_data):
    diff = {}
    keys_status = build_status(primary_data, modified_data)
    for key, value in primary_data.items():
        if key in keys_status[UNMODIFIED]:
            if isinstance(value, dict) and isinstance(modified_data[key],
                                                      dict):
                diff[key] = (NESTED, build_diff(value,
                             modified_data[key]))
            elif value == modified_data[key]:
                diff[key] = (UNMODIFIED, value)
            else:
                diff[key] = safe_put(REPLACED, modified_data[key], value)
        elif key in keys_status[DELETED]:
            diff[key] = safe_put(DELETED, value)
    for key, value in modified_data.items():
        if key in keys_status[ADDED]:
            diff[key] = safe_put(ADDED, value)
    return diff
