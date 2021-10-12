from time import time

from tables.check.base import CheckBase
from tables.models import SimpleTable


def row_generator(rows):
    for _ in range(rows):
        yield SimpleTable(name='testname')


class CheckBulkDelete(CheckBase):
    name = 'bulk_delete'
    graph_title = 'Bulk delete'

    def check_rows(self, rows):
        SimpleTable.objects.all().delete()
        SimpleTable.objects.bulk_create(row_generator(rows))
        start_time = time()
        SimpleTable.objects.all().delete()
        time_taken = time() - start_time
        return time_taken
