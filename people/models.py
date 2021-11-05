from django.db import models


class Person(models.Model):
    name = models.TextField()
    site = models.ForeignKey("Site", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Observatory(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.TextField()
    observatory = models.ForeignKey("Observatory", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
