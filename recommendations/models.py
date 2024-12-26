from django.db import models

# Create your models here.
class Recommendation(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    content_id = models.CharField(max_length=100)  # ID del video o contenido recomendado
    reason = models.TextField()  # Razón de la recomendación
    created_at = models.DateTimeField(auto_now_add=True)
