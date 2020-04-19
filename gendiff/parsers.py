import json
import yaml
import os

SUPPORTED_FORMATS = (JSON, YAML, YML) = ('.json', '.yaml', '.yml')


def get_data(source_file):
    file_format = os.path.splitext(source_file)[1]
    if file_format not in SUPPORTED_FORMATS:
        raise Exception('This file format is not supported.')
    else:
        return _parse_data(file_format, source_file)


def _parse_data(file_format, source_file):
    with open(source_file, 'r') as f:
        if file_format == JSON:
            return json.load(f)
        elif file_format in (YAML, YML):
            return yaml.safe_load(f)
