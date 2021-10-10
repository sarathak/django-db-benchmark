from django.core.management.base import BaseCommand
from time import time, sleep
from tables.models import SimpleTable
from django.conf import settings
import json
from os import path

from tables.benchmarks.insert import benchmark_inserts


def get_file_name(name):
    return path.join(settings.BASE_DIR, f'reports/data/{settings.DB_ENGINE}_{name}.json')


class Command(BaseCommand):
    def handle(self, *args, **options):
        sleep(5)
        insert_times = benchmark_inserts()
        with open(get_file_name('insert'), 'w') as fs:
            json.dump(insert_times, fs)
