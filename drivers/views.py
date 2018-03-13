from django.shortcuts import render

from rest_framework import viewsets

from .models import Driver
from .serializers import DriverSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all().order_by('-name')
    serializer_class = DriverSerializer
