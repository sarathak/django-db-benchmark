from time import time

from tables.check.base import CheckBase
from tables.models import SimpleTable


def row_generator(rows):
    for _ in range(rows):
        yield SimpleTable(name='testname')


class CheckBulkUpdate(CheckBase):
    name = 'bulk_update'
    graph_title = 'Bulk update'

    def check_rows(self, rows):
        SimpleTable.objects.all().delete()
        SimpleTable.objects.bulk_create(row_generator(rows))
        start_time = time()
        SimpleTable.objects.all().update(name='newname')
        time_taken = time() - start_time
        return time_taken
