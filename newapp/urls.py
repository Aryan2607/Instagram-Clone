from turtle import update
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index_view, name="Homepage"),
    path('new/', new_view, name="newpage"),
    path('student/', student_info, name="student page"),
    path('student/edit/<int:id>', edit, name="edit"),
    path('student/update/<int:id>', update, name="Update"),
    path('<id>/delete', delete, name="Delete"),
]
