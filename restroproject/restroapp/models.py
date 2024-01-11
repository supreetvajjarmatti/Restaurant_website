# models.py
from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    datetime = models.DateTimeField()
    no_of_people = models.IntegerField()
    special_request = models.TextField()
