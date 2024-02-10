from django.db import models
import json

# Create your models here.
class Profile(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  location = models.CharField(max_length=50)
  phone = models.IntegerField()
  #add user model here
  def __str__(self):
    return self.name
  

class Animal(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    breed = models.JSONField(default=dict)
    age = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    gender = models.CharField(max_length=100)
    color = models.JSONField(default=dict)
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250, null=True, blank=True)
    photos = models.JSONField(default=list)
    contact = models.JSONField(default=dict)

    def __str__(self):
     return self.name
   

class Favorite(models.Model):

     animalId = models.ForeignKey(Animal, on_delete=models.CASCADE,)

