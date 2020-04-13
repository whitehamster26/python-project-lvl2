import json
import yaml
import os


def get_data(source_file):
    file_format = os.path.splitext(source_file)[1]
    return _parse_data(file_format, source_file)


def _parse_data(format, source_file):
    with open(source_file, 'r') as f:
        if format == '.json':
            return json.load(f)
        elif format in ('.yaml', '.yml'):
            return yaml.safe_load(f)
        else:
            raise Exception('Fromat is not supported.')
