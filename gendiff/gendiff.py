KEYS_STATUS = (COMMON, DELETED, ADDED, REPLACED, NESTED) = (
    'unmodified', 'deleted', 'added', 'replaced', 'nested'
)


def build_tree(data):
    result = {}
    for key in data:
        if isinstance(data[key], dict):
            result[key] = (NESTED, build_tree(data[key]))
        else:
            result[key] = (COMMON, data[key])
    return result


def safe_put(status, value, second_value=None):
    if second_value:
        if isinstance(value, dict) and not isinstance(second_value, dict):
            return status, build_tree(value), second_value
        elif not isinstance(value, dict) and isinstance(second_value, dict):
            return status, value, build_tree(second_value)
    if isinstance(value, dict):
        return status, build_tree(value)
    else:
        return status, value


def build_diff(primary_data, modified_data):
    diff = {}
    keys_status = {}
    keys_status[COMMON] = primary_data.keys() & modified_data.keys()
    keys_status[DELETED] = primary_data.keys() - modified_data.keys()
    keys_status[ADDED] = modified_data.keys() - primary_data.keys()
    for key, value in primary_data.items():
        if key in keys_status[COMMON]:
            if isinstance(value, dict) and isinstance(modified_data[key],
                                                      dict):
                diff[key] = (NESTED, build_diff(value,
                             modified_data[key]))
            elif value == modified_data[key]:
                diff[key] = (COMMON, value)
            else:
                diff[key] = safe_put(REPLACED, modified_data[key], value)
        elif key in keys_status[DELETED]:
            diff[key] = safe_put(DELETED, value)
    for key, value in modified_data.items():
        if key in keys_status[ADDED]:
            diff[key] = safe_put(ADDED, value)
    return diff
