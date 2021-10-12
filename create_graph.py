import json
from os import path
from pathlib import Path

import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent



def get_file_name(engin, name):
    return path.join(BASE_DIR, f'reports/data/{engin}_{name}.json')





if __name__ == '__main__':
    create_graph('insert')
    create_graph('bulk_insert')
    create_graph('bulk_delete')
