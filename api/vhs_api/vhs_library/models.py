from django.db import models

# Create your models here.

class Director(models.Model):
    first_name = models.CharField(max_length = 75)
    last_name = models.CharField(max_length = 75)
    middle_name = models.CharField(max_length = 75)
    comment = models.TextField(blank = True, max_length=1000)


class Actor(models.Model):
    first_name = models.CharField(max_length = 75)
    last_name = models.CharField(max_length = 75)
    middle_name = models.CharField(max_length = 75)
    comment = models.TextField(blank = True, max_length = 1000)


class Studio(models.Model):
    name = models.CharField(max_length = 100)
    comment = models.TextField(blank = True, max_length = 1000)


class Distributor(models.Model):
    name = models.CharField(max_length = 100)
    comment = models.TextField(blank = True, max_length = 1000)


class Genre(models.Model):
    name = models.CharField(max_length = 100)
    comment = models.TextField(blank = True, max_length = 1000)


class BoxSet(models.Model):
    name = models.CharField(max_length = 100)
    comment = models.TextField(blank = True, max_length = 1000)

class Network(models.Model):
    name = models.CharField(max_length = 50)
    comment = models.TextField(blank = True, max_length = 1000)


class Movie(models.Model):
    directors = models.ManyToManyField(Director, blank= True, db_index= True)
    actors = models.ManyToManyField(Actor, blank = True)
    studios = models.ManyToManyField(Studio, blank = True)
    distributors = models.ManyToManyField(Distributor, blank = True)
    genres = models.ManyToManyField(Genre, max_length = 75)
    box_set = models.ManyToManyField(BoxSet, blank = True)
    network = models.ForeignKey(Network, blank = True, null = True, on_delete = models.SET_NULL)
    origin = models.CharField(max_length = 50)
    television = models.BooleanField(default = False)
    medium = models.CharField(max_length = 50)
    title = models.CharField(max_length = 100)
    for_rent = models.BooleanField(default = False)
    on_loan = models.BooleanField(default = False)
    