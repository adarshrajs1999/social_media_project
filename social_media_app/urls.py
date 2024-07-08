from django.urls import path
from social_media_app import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('dash/',views.dash, name = 'dash'),
   
    
]

