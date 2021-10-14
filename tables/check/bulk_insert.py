from time import time

from tables.check.base import CheckBase
from tables.models import SimpleTable


class CheckBulkInsert(CheckBase):
    name = 'bulk_insert'
    graph_title = 'Bulk insert'

    def check_rows(self, rows):
        start_time = time()
        values = (SimpleTable(name='testname') for _ in range(rows))
        SimpleTable.objects.bulk_create(values)
        time_taken = time() - start_time
        return time_taken
