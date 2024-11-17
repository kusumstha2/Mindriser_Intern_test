from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username','email','first_name','last_name','is_staff','role',)
    search_fields =('username','email','first_name','last_name',)
    list_per_page=5
