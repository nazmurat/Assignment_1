from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('task/',task,name="task"),
    path('update/<str:pk>/', update, name = "update"),
    path('delete/<str:pk>/', delete, name = "delete"),
]