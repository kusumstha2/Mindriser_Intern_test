from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    user_choice = (
        ('Admin','Admin'),
        ('Staff','Staff'),
    )
    
    role = models.CharField(max_length=50,choices=user_choice,default='Admin')
    name = models.CharField(max_length=50)
    REQUIRED_FIELDS =[
        'role',
    ]
