from .models import User, Job
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','name', 'username', 'phone_no',  'user_type')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['email','name', 'username', 'phone_no',  'user_type','password' ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password']