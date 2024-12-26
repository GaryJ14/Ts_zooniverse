from django.db import models

# Create your models here.
class GeoContent(models.Model):
    video = models.ForeignKey('content.Video', on_delete=models.CASCADE)
    location_name = models.CharField(max_length=255)
    coordinates = models.JSONField()  # Ejemplo: {"latitude": 40.7128, "longitude": -74.0060}
    added_at = models.DateTimeField(auto_now_add=True)
