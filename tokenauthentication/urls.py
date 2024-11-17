from django.urls import path, include
from django.contrib.auth.models import User
from .views import LoginAPIView,LogoutAPIView,RegistrationAPIView


urlpatterns = [
   path('register/',RegistrationAPIView.as_view(),name='user-registration'),
   path('login/',LoginAPIView.as_view(),name='user-login'),
   path('logout/',LogoutAPIView.as_view(),name= 'user-logout'),
   
]