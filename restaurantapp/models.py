from django.db import models

# Create your models here.

class Table(models.Model):
    table_number=models.PositiveIntegerField()
    seating_capacity = models.PositiveBigIntegerField()
    is_available=models.BooleanField(default=True)


    def __str__(self):
        return self.table_number
    



class Category(models.Model):
    VEG = 'Veg'
    NON_VEG = 'Non-Veg'
    CATEGORY_CHOICES = [
        (VEG, 'Vegetarian'),
        (NON_VEG, 'Non-Vegetarian'),
    ]

    name = models.CharField(max_length=50)
    veg_non_veg = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.veg_non_veg


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    


