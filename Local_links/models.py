from django.db import models

# Create your models here.

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    products = models.CharField(max_length=100, choices=[
        ('VEGETABLES', 'Vegetables'),
        ('FRUITS', 'Fruits'),
        ('MEAT', 'Meat'),
        ('DAIRY', 'Dairy')
    ])
    contact = models.EmailField()
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    

