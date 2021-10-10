from django.db import models


class SimpleTable(models.Model):
    name = models.CharField(max_length=50)
