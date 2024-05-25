from .models import *
from rest_framework import serializers


class User_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','first_name','last_name','password']
        read_only_fields=['id']
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class Task_serializer(serializers.ModelSerializer):
    
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Taskmodel
        fields="__all__"
        read_only_fields=['id','status','user','task_date']