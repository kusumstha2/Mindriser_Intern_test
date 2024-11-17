from django.urls import path
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()

router.register(r'table',TableViewSet,basename= "table")
router.register(r'category',CategoryViewSet,basename="category")
router.register(r'menuitem',MenuItemViewSet,basename="menuitem")
urlpatterns = router.urls+[

]
