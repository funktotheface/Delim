from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

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
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10, default='u')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    expiry_date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def clean(self):
        if self.quantity is None:
            raise ValidationError('Quantity must be provided')

        if self.quantity < 0 or self.quantity > 1000:
            raise ValidationError('Quantity must be between 0 and 1000')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name    
    
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta: 
        verbose_name_plural = "Categories"  

    def __str__(self):
        return self.name