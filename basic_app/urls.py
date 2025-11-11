from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('solution1/', views.solution1, name='solution1'), 
    path('contact/', views.contact, name='contact'), 
    path('about/', views.about, name='about'),
   
]