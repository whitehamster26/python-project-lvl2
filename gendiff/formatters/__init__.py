from gendiff.formatters.json import diff_rendering as json # noqa F401
from gendiff.formatters.plain import diff_rendering as plain # noqa F401
from gendiff.formatters.default import diff_rendering as default # noqa F401


FORMATTERS = (JSON, PLAIN, DEFAULT) = (
    'json', 'plain', 'default'
)
