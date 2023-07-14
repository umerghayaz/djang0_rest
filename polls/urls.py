from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('notes/', views.save_data, name="notes"),
    path('update/<id>', views.update_data),
    path('delete_data/<id>', views.delete_data),
]