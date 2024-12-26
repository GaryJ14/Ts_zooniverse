from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.JSONField(null=True, blank=True)  # Etiquetas del video
    uploaded_by = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Metadata(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='metadata')
    key = models.CharField(max_length=100)
    value = models.TextField()
