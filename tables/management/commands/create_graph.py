from time import sleep

from django.core.management.base import BaseCommand

from tables.check import ALL_CHECKS


class Command(BaseCommand):
    def handle(self, *args, **options):
        for check in ALL_CHECKS:
            check().create_graph()
