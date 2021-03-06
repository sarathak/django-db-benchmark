from time import time

from tables.check.base import CheckBase
from tables.models import SimpleTable


class CheckBulkDelete(CheckBase):
    name = 'bulk_delete'
    graph_title = 'Bulk delete'

    def create_rows(self, rows):
        SimpleTable.objects.all().delete()
        values = (SimpleTable(name='testname') for _ in range(rows))
        SimpleTable.objects.bulk_create(values)

    def check_rows(self, rows):
        self.create_rows(rows)
        start_time = time()
        SimpleTable.objects.all().delete()
        time_taken = time() - start_time
        return time_taken
