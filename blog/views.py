from django.shortcuts import render

# Create your views here.
import django_filters
from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer
from rest_framework import viewsets, filters

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer