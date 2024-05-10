from django.db import models
from datetime import datetime, timedelta
import random

class SensorData(models.Model):
    soil_moisture = models.FloatField()
    temperature = models.FloatField()

    class Meta:
        verbose_name_plural = "Sensor Data"

    def __str__(self):
        return f"{self.timestamp} - Soil Moisture: {self.soil_moisture}, Temperature: {self.temperature}"

class MediaContent(models.Model):
    video = models.FileField(upload_to='videos/')
    photo = models.ImageField(upload_to='photos/')

    class Meta:
        verbose_name_plural = "Media Content"

    def __str__(self):
        return f"Video: {self.video.name}, Photo: {self.photo.name}"
    # @staticmethod
    # def generate_dummy_data_and_cleanup():
    #     # Generate dummy data
    #     for _ in range(3):
    #         soil_moisture = random.uniform(0, 100)
    #         temperature = random.uniform(10, 40)
    #         SensorData.objects.create(soil_moisture=soil_moisture, temperature=temperature)

    #     # Calculate cutoff time (20 seconds ago)
    #     twenty_seconds_ago = datetime.now() - timedelta(seconds=20)
        
    #     # Delete old data
    #     SensorData.objects.filter(timestamp__lt=twenty_seconds_ago).delete()
