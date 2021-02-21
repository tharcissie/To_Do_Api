from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('todos', ToDoList.as_view()),
    path('todos/<int:pk>',ToDoDetail.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]