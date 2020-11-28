#!/usr/bin/env python3
import jsonschema
import os
import sys
import yaml

def parse_yaml(path):
    with open(path) as fs:
        text = fs.read()
        return yaml.load_all(text, Loader=yaml.SafeLoader)

def build_schema():
    filter_names = next(parse_yaml('_data/filters.yml')).keys()
    item_names = next(parse_yaml('_data/items.yml')).keys()
    return {
        "definitions": {
            'examples': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'description': {'type': 'string'},
                        'code': {'type': 'string'},
                    },
                    'additionalProperties': False
                },
                'minimum': 1
            }
        },
        'type': 'object',
        'properties': {
            'description': {'type': 'string'},
            'items': {
                'type': 'object',
                "patternProperties": {
                    '^({})$'.format('|'.join(item_names)): {'$ref': '#/definitions/examples'}
                },
                'additionalProperties': False
            },
            'filters': {
                'type': 'object',
                "patternProperties": {
                    '^({})$'.format('|'.join(filter_names)): {'$ref': '#/definitions/examples'}
                },
                'additionalProperties': False
            }
        },
        'required': ['items'],
        'additionalProperties': False
    }

def validate_directory(root):
    schema = build_schema()
    root, _, files = next(os.walk(root))
    for name in files:
        if not name.endswith('.md'):
            continue
        path = os.path.join(root, name)
        data = parse_yaml(path)
        try:
            jsonschema.validate(next(data), schema)
        except jsonschema.exceptions.ValidationError as err:
            print('{}: {}'.format(name, err))
            sys.exit(1)

if __name__ == '__main__':
    validate_directory("_wadcoms/")
