from rest_framework import serializers
from .models import ToDo


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