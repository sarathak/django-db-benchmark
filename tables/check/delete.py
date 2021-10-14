from time import time

from tables.check.base import CheckBase
from tables.models import SimpleTable


class CheckDelete(CheckBase):
    name = 'delete'
    graph_title = 'Delete'

    def create_rows(self, rows):
        SimpleTable.objects.all().delete()
        values = (SimpleTable(name='testname') for _ in range(rows))
        SimpleTable.objects.bulk_create(values)

    def check_rows(self, rows):
        self.create_rows(rows)
        start_pk = SimpleTable.objects.all().order_by('id')[0].pk
        start_time = time()
        for i in range(rows):
            SimpleTable.objects.filter(pk=start_pk + i).delete()
        time_taken = time() - start_time
        return time_taken
