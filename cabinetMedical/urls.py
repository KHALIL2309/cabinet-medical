from django.urls import path
from . import views

urlpatterns = [
    path('client/', views.client), 
    path('about/', views.about), 
    path('user/', views.user), 
    path('page/', views.page), 
    path('home/', views.home), 
    path('book/', views.boook), 
    path('', views.projet3), 
]