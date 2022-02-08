from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from price_prediction import views

urlpatterns = [


    path("", views.index , name='price_prediction'),
    path("about", views.about,name='about'),
    path("contact", views.contact,name='contact'),
    path("services", views.services,name='services'),
    path("login", views.login,name='login'),
    
    
]