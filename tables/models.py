from django.db import models


class SimpleTable(models.Model):
    name = models.CharField(max_length=50)


class SimpleIndexedTable(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    other_name = models.CharField(max_length=50)
