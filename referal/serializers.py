from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'date_joined']

class ObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        if hasattr(user, 'profile'):
            token['middle_name'] = user.profile.middle_name
            token['email'] = user.email
            token['mobile'] = user.profile.mobile

        return token

class BackgroundInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundInformation
        fields = '__all__'  # Includes all fields

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'  # Includes all fields

class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'  # Includes all fields

class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = '__all__'  # Includes all fields

    
