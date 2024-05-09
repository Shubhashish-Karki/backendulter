from rest_framework import serializers
from . import models

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.SensorData
        fields = ['id','timestamp','soil_moisture','temperature']