import os.path

import matplotlib.pyplot as plt
from pathlib import Path
from os import path
import json

BASE_DIR = Path(__file__).resolve().parent
DB_ENGINES = ['postgresql', 'mysql','mariadb']


def get_file_name(engin, name):
    return path.join(BASE_DIR, f'reports/data/{engin}_{name}.json')


def create_graph(name):
    fig, ax = plt.subplots()
    ax.set_ylabel('Time(s)')
    ax.set_xlabel('Rows')
    for engin in DB_ENGINES:
        file_name = get_file_name(engin, name)
        if not path.isfile(file_name):
            continue
        with open(file_name, 'r') as fs:
            data = json.load(fs)
            x = list(map(lambda item: item['rows'], data))
            y = list(map(lambda item: item['time'], data))
            ax.plot(x, y, label=engin)
    ax.set_title('Insert time')
    ax.legend()
    file_name = path.join(BASE_DIR, f'reports/graphs/{name}.png')
    plt.savefig(path.join(BASE_DIR, f'reports/graphs/{name}.png'), format='png')
    print('file saved', file_name)


if __name__ == '__main__':
    create_graph('insert')
