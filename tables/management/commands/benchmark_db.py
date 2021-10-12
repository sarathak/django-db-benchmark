from time import sleep

from django.core.management.base import BaseCommand

from tables.check import ALL_CHECKS


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("benchmark will start in 5 seconds")
        sleep(5)
        for check in ALL_CHECKS:
            check().run()
