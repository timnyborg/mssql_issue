from django.db import models


class Person(models.Model):
    nationality = models.IntegerField()
