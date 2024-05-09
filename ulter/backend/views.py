from urllib import request
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import SensorDataSerializer
from . import models

# Create your views here.
def SensorDataList(request):
    sensor_data = models.SensorData.objects.all()
    serializer = SensorDataSerializer(sensor_data, many=True)
    return JsonResponse(serializer.data, safe=False)


class SensorDataDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = models.SensorData.objects.all()
   serializer_class = SensorDataSerializer

