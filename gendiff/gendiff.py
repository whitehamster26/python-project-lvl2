def generate_diff(primary_data, modified_data):
    diff = {}
    for key in primary_data:
        if key in modified_data:
            if primary_data[key] == modified_data[key]:
                diff[key] = ('unmodified', primary_data[key])
            else:
                if isinstance(primary_data[key], dict) and \
                        isinstance(modified_data[key], dict):
                    diff[key] = ('nested', generate_diff(
                        primary_data[key], modified_data[key]))
                else:
                    diff[key] = ('replaced', modified_data[key],
                                 primary_data[key])
        elif key not in modified_data:
            if isinstance(primary_data[key], dict):
                diff[key] = ('deleted', generate_diff(
                    primary_data[key],
                    primary_data[key]))
            else:
                diff[key] = ('deleted', primary_data[key])
    for key in modified_data:
        if key not in primary_data:
            if isinstance(modified_data[key], dict):
                diff[key] = ('added', generate_diff(
                    modified_data[key],
                    modified_data[key]))
            else:
                diff[key] = ('added', modified_data[key])
    return diff
