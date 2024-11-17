from django.shortcuts import render
from .models import *
# Create your views here.
from rest_framework  import viewsets,filters
from .serializer import TableSerializer,CategorySerializer,MenuItemSerializer
from  rest_framework.pagination import PageNumberPagination
from .permission import isAdminReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter



class TableViewSet(viewsets.ModelViewSet):
    queryset= Table.objects.all()
    serializer_class = TableSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,DjangoFilterBackend)
    search_field =('table_number',)
    permission_classes=(isAdminReadOnly,)
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,DjangoFilterBackend)
    search_field =('name',)
    permission_classes =(isAdminReadOnly,)
    

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset= MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,DjangoFilterBackend)
    search_field =('name',)
    permission_classes =(isAdminReadOnly,)
        
    