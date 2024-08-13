from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse, FileResponse
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import *
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission
from django.http import FileResponse, Http404
from collections import defaultdict
from .models import User
from rest_framework.authentication import TokenAuthentication
import logging
import os
from django.conf import settings
from django.utils.dateparse import parse_duration
from django.db.models import Avg
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class ObtainPairView(TokenObtainPairView):
    serializer_class = ObtainSerializer

class AllUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# background Information
class post_basic(APIView):
    queryset = BackgroundInformation.objects.all()
    serializer_class = BackgroundInformationSerializer

    def post(self, request, format=None):
        user = request.data.get('user')
        if BackgroundInformation.objects.filter(user=user).exists():
            return Response({"error": "Background information already exists for this user."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializers = BackgroundInformationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# Bussiness information
class post_bussiness(APIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    def post(self, request, format=None):
        user = request.data.get('user')
        if Business.objects.filter(user=user).exists():
            return Response({"error": "Bussiness information already exists for this user."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializers =BusinessSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#services
class services(generics.ListAPIView):
  queryset =Services.objects.all()
  serializer_class = ServicesSerializer

class post_services(APIView):
    queryset =Services.objects.all()
    serializer_class = ServicesSerializer

    def post(self, request, format=None):
        user = request.data.get('user')
        if Services.objects.filter(user=user).exists():
            return Response({"error": "Services information already exists for this user."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializers =ServicesSerializer(data=request.data)
        if serializers.is_valid():
            service = serializers.save()
            send_welcome_email(service )
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#modules
class Modules(generics.ListAPIView):
    queryset = Modules.objects.all()
    serializer_class = ModulesSerializer


def send_welcome_email(user):
    subject = "Welcome to Grow"
    message = f"Dear {user.first_name},\n\nWelcome to Grow. Your Application has beeen successfully received thank you for applying with GROW we promise you all the best."
    from_email = settings.EMAIL_HOST_USER
    to_email = [user.email]
    send_mail(subject, message, from_email, to_email, fail_silently=False)
    
