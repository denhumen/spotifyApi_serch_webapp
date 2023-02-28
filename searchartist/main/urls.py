from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='search'),
    path('map/', views.shopwmap, name="map_page"),
]