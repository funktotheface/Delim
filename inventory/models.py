from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class InventoryItem(models.Model):
    UNIT_CHOICES = [
        ('g', 'grams'),
        ('kg', 'kilograms'),
        ('ml', 'milliliters'),
        ('l', 'liters'),
        ('u', 'unit'),
        ('oz', 'ounces'),
    ]
    name = models.CharField(max_length=200)
    quantity = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1000.0)]
    )
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default='u')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    expiry_date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name    
    
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta: 
        verbose_name_plural = "Categories"  

    def __str__(self):
        return self.name