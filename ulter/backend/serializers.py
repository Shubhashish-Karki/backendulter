from rest_framework import serializers
from . import models

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.SensorData
        fields = ['soil_moisture','temperature']

class MediaContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MediaContent
        fields = ['video', 'photo']