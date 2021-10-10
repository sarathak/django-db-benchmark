from time import time

from django.conf import settings

from tables.models import SimpleTable

ROWS_LIST = [10, 100, 1000, 10000]


def get_insert_time(rows):
    print(f'Testing inset time {rows}')
    start_time = time()
    for _ in range(rows):
        SimpleTable.objects.create(name='testname')
    time_taken = time() - start_time
    print(f'completed in {time_taken}')
    return time_taken


def benchmark_inserts():
    print(f"Benchmarking {settings.DB_ENGINE} insets")
    data = []
    for rows in ROWS_LIST:
        time_taken = get_insert_time(rows)
        data.append(dict(
            rows=rows,
            time=time_taken,
        ))
    return data
