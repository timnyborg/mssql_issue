from django.db import models


class Person(models.Model):
    nationality = models.ForeignKey(
        "Nationality", on_delete=models.DO_NOTHING, db_column="nationality"
    )


class Nationality(models.Model):
    name = models.CharField(max_length=100)
