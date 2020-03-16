import json


def generate_diff(first_file, second_file, format=None):
    first_file_data = json.load(open(first_file))
    second_file_data = json.load(open(second_file))
    result = '{' + '\n'
    for key in first_file_data:
        if key in second_file_data:
            if first_file_data[key] == second_file_data[key]:
                result = result + (f'    {key}: {first_file_data[key]}\n')
            else:
                result = result + (f'  + {key}: {second_file_data[key]}\n')
                result = result + (f'  - {key}: {first_file_data[key]}\n')
        elif key not in second_file_data:
            result = result + (f'  - {key}: {first_file_data[key]}\n')
    for key in second_file_data:
        if key not in first_file_data:
            result = result + (f'  + {key}: {second_file_data[key]}\n')
    result = result + '}'
    return result


def show_difference(first_file, second_file, format=None):
    print(generate_diff(first_file, second_file, format=None))
    return None
