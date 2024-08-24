from rest_framework import serializers
from django.contrib.auth.models import User

from django.contrib.auth import authenticate

class SignupSerializer(serializers.Serializer):
    email = serializers.CharField()
    username = serializers.CharField()
    password=serializers.CharField()
    
    def validate(self, data):
        
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('username is taken') 
        
        return data
    
    def create(self,validated_data):
        user=User.objects.create(
                                 username=validated_data['username'],
                                 email=validated_data['email'],)
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
    
    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password=serializers.CharField()
    
    def validate(self, data):
        
        if not User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('user does not exists') 
        
        return data
    

        
