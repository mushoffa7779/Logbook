from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views
urlpatterns = [
    path('mitra/', views.mitra),
    path('mitra/new/', views.new),
    path('mitra/mitra/<id>/', views.detail),
    path('mitra/mitra/<id>/delete/', views.delete),
    path('mitra/mitra/<id>/update/', views.update),
]
