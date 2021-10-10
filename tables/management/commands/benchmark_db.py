from django.core.management.base import BaseCommand
from time import time
from tables.models import SimpleTable


class Command(BaseCommand):
    def handle(self, *args, **options):
        t = time()
        for _ in range(100):
            SimpleTable.objects.create(name='testname')

        print(time() - t)
