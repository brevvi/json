#!/usr/bin/env python

import json

data = {
    'presidente': {
        'name': 'Zaphod Beelebrox',
        'species': 'Betelgeusian'
    }
}

with open('data_file.json', 'w') as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data)


