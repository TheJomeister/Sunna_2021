from django.urls import path

from . import views 

URLPatterns = [
    path('create-todo', views.create_todo, 'create-todo')
]