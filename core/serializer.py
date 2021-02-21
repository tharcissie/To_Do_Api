from rest_framework import serializers
from .models import ToDo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=ToDo.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'todos']


class ToDoSerializer(serializers.ModelSerializer):

    PRIORITY = (
        ('LOW','LOW'),
        ('MEDIUM','MEDIUM'),
        ('HIGH','HIGH')
    )

    priority = serializers.ChoiceField( choices = PRIORITY)

    class Meta:
        model = ToDo
        fields =('id','title','description','priority','created_date','modified_date')