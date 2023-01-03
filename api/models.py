from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=200)
    height = models.IntegerField()
    mass = models.IntegerField()
    hair_color = models.CharField(max_length=30)
    eye_color = models.CharField(max_length=30)
    birth_year = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    homeworld = models.URLField()
    films = models.CharField(max_length=300)
    species = models.CharField(max_length=30)
    vehicles = models.CharField(max_length=300)
    starships = models.CharField(max_length=300)
    created = models.DateTimeField()
    edited = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return self.name

