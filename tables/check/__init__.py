from tables.check.insert import CheckInsert
from tables.check.bulk_insert import CheckBulkInsert

ALL_CHECKS = (CheckInsert, CheckBulkInsert,)
ALL_NAMES = [x.name for x in ALL_CHECKS]
