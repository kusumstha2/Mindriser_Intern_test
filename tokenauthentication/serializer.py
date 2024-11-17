from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        
        fields= (
           'email', 
           'username',
           'role', 'password',
        )  
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
        
        model = User