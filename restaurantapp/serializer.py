from rest_framework import serializers
from .models import *
class TableSerializer(serializers.ModelSerializer):
    class Meta:
       
        fields = ('table_number',
                  'seating_capacity',
                  'is_available',
        )   
        model = Table
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
       
        fields = ('name',
                  'veg_non_veg',)
        model = Category
       
        
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
       
        fields = ('name',
                  'description',
                  'price',
                  'category',
                  'is_available',)
        model = MenuItem
                      