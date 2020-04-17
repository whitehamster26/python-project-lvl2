from gendiff.formatters.json import render_json as json # noqa F401
from gendiff.formatters.plain import render_diff as plain # noqa F401
from gendiff.formatters.default import render_diff as default # noqa F401


FORMATTERS = (JSON, PLAIN, DEFAULT) = (
    'json', 'plain', 'default'
)
