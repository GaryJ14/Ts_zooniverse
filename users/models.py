from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    location = models.CharField(max_length=255, null=True, blank=True)
    profile_data = models.JSONField(null=True, blank=True)
    user_type = models.CharField(max_length=50, choices=[
        ('regular_user', 'Regular User'),
        ('admin', 'Admin'),
        ('zooniverse_admin', 'Zooniverse Admin')
    ])
    