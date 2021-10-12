from time import time

from tables.check.base import CheckBase
from tables.models import SimpleTable


def row_generator(rows):
    for _ in range(rows):
        yield SimpleTable(name='testname')


class CheckBulkInsert(CheckBase):
    name = 'bulk_insert'

    def check_rows(self, rows):
        start_time = time()
        SimpleTable.objects.bulk_create(row_generator(rows))
        time_taken = time() - start_time
        return time_taken
