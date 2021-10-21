from time import time

from tables.check.base import CheckBase
from tables.models import SimpleIndexedTable


class CheckSelectIndex(CheckBase):
    name = 'select_index'
    graph_title = 'Select indexed'

    def check_rows(self, rows):
        SimpleIndexedTable.objects.all().delete()
        values = (SimpleIndexedTable(name=f'test{i}', other_name='other') for i in range(rows))
        SimpleIndexedTable.objects.bulk_create(values)
        start_time = time()
        for i in range(rows):
            SimpleIndexedTable.objects.get(name=f'test{i}')
        time_taken = time() - start_time
        return time_taken
