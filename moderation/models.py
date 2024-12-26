from django.db import models

# Create your models here.
class VideoQualityAssessment(models.Model):
    video = models.OneToOneField('content.Video', on_delete=models.CASCADE, related_name='quality')
    audio_score = models.FloatField()  # Puntaje de calidad de audio
    video_score = models.FloatField()  # Puntaje de calidad de video

class NudityDetection(models.Model):
    video = models.ForeignKey('content.Video', on_delete=models.CASCADE)
    contains_nudity = models.BooleanField()
    detected_at = models.DateTimeField(auto_now_add=True)

class CopyrightValidation(models.Model):
    video = models.ForeignKey('content.Video', on_delete=models.CASCADE)
    is_copyrighted = models.BooleanField()
    validated_at = models.DateTimeField(auto_now_add=True)
