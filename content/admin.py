# Register your models here.
from django.contrib import admin
from .models import Video, Metadata  # Cambia según la aplicación

admin.site.register(Video)
admin.site.register(Metadata)
