from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Thing(models.Model):
    name = models.CharField(
        max_length = 30,
        blank = False, 
        unique = False,                
    )
    description = models.CharField(
        max_length = 120,
        blank = False, 
        unique = False,                
    )
    quantity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )