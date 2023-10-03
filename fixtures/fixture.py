import json


def get_fixture(name):
    data = []
    with open(f'fixtures/{name}.json', 'r') as f:
        data = json.load(f)
    return data
