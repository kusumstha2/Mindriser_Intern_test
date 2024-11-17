from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display=('table_number','seating_capacity','is_available',)
    search_fields=('table number','is_available',)
    list_filter =('is_available',)
    list_per_page = 5
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','veg_non_veg',)
    search_fields=('name',)
    list_filter =('name',)
    list_per_page = 5
    
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display=('name','description','price','category','is_available',)
    search_fields=('name','category',)
    list_filter =('name',)
    list_per_page = 5
 
    