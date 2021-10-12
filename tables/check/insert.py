from time import time

from tables.check.base import CheckBase
from tables.models import SimpleTable


class CheckInsert(CheckBase):
    name = 'insert'
    def check_rows(self, rows):
        start_time = time()
        for _ in range(rows):
            SimpleTable.objects.create(name='testname')
        time_taken = time() - start_time
        return time_taken
