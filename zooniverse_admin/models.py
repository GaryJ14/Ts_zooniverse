from django.db import models

# Create your models here.
class AnimalClassification(models.Model):
    image = models.ImageField(upload_to='animal_images/')
    species = models.CharField(max_length=255)
    attributes = models.JSONField()  # Ejemplo: {"color": "brown", "size": "large"}
    count = models.IntegerField(default=1)  # Número de animales detectados

class PlanktonClassification(models.Model):
    image = models.ImageField(upload_to='plankton_images/')
    species = models.CharField(max_length=255)
    detected_at = models.DateTimeField(auto_now_add=True)

class SubjectGroup(models.Model):
    subject_id = models.CharField(max_length=100)  # ID del sujeto en Zooniverse
    similarity_score = models.FloatField()  # Nivel de similitud con otros sujetos
    grouped_at = models.DateTimeField(auto_now_add=True)

class ProjectRecommendation(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    recommended_at = models.DateTimeField(auto_now_add=True)
