from time import time

from tables.check.base import CheckBase
from tables.models import SimpleTable


class CheckSelect(CheckBase):
    name = 'select'
    graph_title = 'Select non indexed'

    def check_rows(self, rows):
        SimpleTable.objects.all().delete()
        values = (SimpleTable(name=f'test{i}') for i in range(rows))
        SimpleTable.objects.bulk_create(values)
        start_time = time()
        for i in range(rows):
            SimpleTable.objects.get(name=f'test{i}')
        time_taken = time() - start_time
        return time_taken
