from tables.check.bulk_update import CheckBulkUpdate
from tables.check.delete import CheckDelete
from tables.check.insert import CheckInsert
from tables.check.bulk_insert import CheckBulkInsert
from tables.check.bulk_delete import CheckBulkDelete
from tables.check.update import CheckUpdate

ALL_CHECKS = (CheckInsert, CheckBulkInsert, CheckBulkDelete, CheckUpdate, CheckBulkUpdate, CheckDelete)
ALL_NAMES = [x.name for x in ALL_CHECKS]
