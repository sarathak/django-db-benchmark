from time import time

from tables.check.base import CheckBase
from tables.models import SimpleTable


class CheckBulkUpdate(CheckBase):
    name = 'bulk_update'
    graph_title = 'Bulk update'

    def check_rows(self, rows):
        SimpleTable.objects.all().delete()
        values = (SimpleTable(name='testname') for _ in range(rows))
        SimpleTable.objects.bulk_create(values)
        start_time = time()
        SimpleTable.objects.all().update(name='newname')
        time_taken = time() - start_time
        return time_taken
