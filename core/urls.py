from django.urls import path
from .views import *

urlpatterns = [
    path('todos', ToDoList.as_view()),
    path('todos/<int:pk>',ToDoDetail.as_view())
]