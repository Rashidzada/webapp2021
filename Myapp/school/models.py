from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=30)
    father = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    contact = models.CharField(max_length=11)
    intro = models.TextField()
    email = models.EmailField()
    def __str__(self):
        return self.name