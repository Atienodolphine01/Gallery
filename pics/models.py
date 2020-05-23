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

class Picture(models.Model):
    Picture = models.PictureField(upload_to='images/',null=True)
    picture_name = models.CharField(max_length=255)
    picture_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def save_Picture(self):
        self.save()

    def delete_Picture(self):
        self.delete()


    
