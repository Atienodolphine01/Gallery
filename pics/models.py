from django.db import models

# Create your models here.
class Location(models.Model):
    place = models.CharField(max_length=255) #input location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.place


class Category(models,Model):
    name = models.CharField(max_length=255)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name
 

    
