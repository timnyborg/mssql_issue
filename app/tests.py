from django import test

from . import models


class BasicTest(test.TestCase):
    def test(self):
        nation = models.Nationality.objects.create(name="UK")
        models.Person.objects.create(nationality=nation)
