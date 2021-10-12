from time import time

from tables.check.base import CheckBase
from tables.models import SimpleTable


class CheckUpdate(CheckBase):
    name = 'update'
    graph_title = 'Update'

    def check_rows(self, rows):
        m = SimpleTable.objects.create(name='testname')
        start_time = time()
        for i in range(rows):
            m.name = f'name{i}'
            m.save()
        time_taken = time() - start_time
        return time_taken
