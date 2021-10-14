from django.test.testcases import override_settings, TestCase
from unittest.mock import patch
from tables.check import CheckBulkDelete, CheckBulkInsert
from tables.models import SimpleTable


class TestCheck(TestCase):
    @override_settings(ROWS_LIST=[2, 3, 4])
    @patch('tables.check.bulk_delete.CheckBulkDelete.check_rows', return_value=1)
    def test_check_all(self, *args):
        check = CheckBulkDelete()
        time_list = check.check_all()
        self.assertListEqual(time_list, [
            {'rows': 2, 'time': 1},
            {'rows': 3, 'time': 1},
            {'rows': 4, 'time': 1}
        ])

    def test_bulk_delete_create_rows(self):
        check = CheckBulkDelete()
        SimpleTable.objects.bulk_create((SimpleTable(name='22') for _ in range(3)))
        check.create_rows(2)
        self.assertEqual(SimpleTable.objects.all().count(), 2)

    def test_bulk_delete(self):
        check = CheckBulkDelete()
        check.check_rows(2)
        self.assertEqual(SimpleTable.objects.all().count(), 0)

    def test_check_rows(self):
        check = CheckBulkInsert()
        check.check_rows(2)
        self.assertEqual(SimpleTable.objects.all().count(), 2)
