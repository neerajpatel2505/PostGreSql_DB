from django.db import models

# Create your models here.
class DataStore(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Age = models.CharField(max_length=200)
    Qualification = models.CharField(max_length=200)
    DOB = models.DateField()
    Language_Known = models.CharField(max_length=200)
    
    def __str__(self):
        return self.First_Name