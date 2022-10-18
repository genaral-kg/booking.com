from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import  permissions
from .models import City
from . import serializers



class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = serializers.CitySerializer


    def get_permissions(self):
        if self.action in ('retrieve','list'):
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]

