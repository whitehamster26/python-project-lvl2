import json
import yaml


def parse_format(file_name):
    dot_index = file_name.rfind('.')
    file_format = file_name[dot_index+1:len(file_name)]
    if file_format == 'yml':
        return 'yaml'
    return file_format


def json_parse(first_file, second_file):
    first_file_data = json.load(open(first_file))
    second_file_data = json.load(open(second_file))
    return first_file_data, second_file_data


def yaml_parse(first_file, second_file):
    first_file_data = yaml.safe_load(open(first_file))
    second_file_data = yaml.safe_load(open(second_file))
    return first_file_data, second_file_data


def parse_data(format, first_file, second_file):
    if format:
        if format == 'json':
            return json_parse(first_file, second_file)
        elif format == 'yaml':
            return yaml_parse(first_file, second_file)
