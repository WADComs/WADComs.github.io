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
    service_names = next(parse_yaml('_data/services.yml')).keys()
    item_names = next(parse_yaml('_data/items.yml')).keys()
    OS_names = next(parse_yaml('_data/OS.yml')).keys()
    attack_names = next(parse_yaml('_data/attack_types.yml')).keys()
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
            'command': {'type': 'string'},
            'items': {
                'type': 'array',
                "patternProperties": {
                    '^({})$'.format('|'.join(item_names)): {'$ref': '#/definitions/examples'}
                },
                'additionalProperties': False
            },
            'services': {
                'type': 'array',
                "patternProperties": {
                    '^({})$'.format('|'.join(service_names)): {'$ref': '#/definitions/examples'}
                },
                'additionalProperties': False
            },
            'OS': {
                'type': 'array',
                "patternProperties": {
                    '^({})$'.format('|'.join(OS_names)): {'$ref': '#/definitions/examples'}
                },
                'additionalProperties': False
            },
            'attack_types': {
                'type': 'array',
                "patternProperties": {
                    '^({})$'.format('|'.join(attack_names)): {'$ref': '#/definitions/examples'}
                },
                'additionalProperties': False
            },
            'references': {
                'type': 'array',
                'additionalProperties': False
            }
        },
        'required': ['items', 'command', 'OS'],
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
