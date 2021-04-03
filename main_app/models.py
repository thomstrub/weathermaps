from django.db import models

# Create your models here.
class Map(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100)
    elevation = models.IntegerField()

    def __str__(self):
        return self.name
        