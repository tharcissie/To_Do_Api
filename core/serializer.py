from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        mdel = ToDo
        fields =('id','title','description','priority','created_date','modified_date')