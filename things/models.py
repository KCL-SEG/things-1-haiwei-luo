from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(
        max_length = 20,
        blank = False, 
        unique = False,                
    )
    description = models.CharField(
        max_length = 50,
        blank = False, 
        unique = False,                
    )
    quantity = models.IntegerField()