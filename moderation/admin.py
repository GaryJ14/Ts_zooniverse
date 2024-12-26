from django.contrib import admin
from .models import VideoQualityAssessment, NudityDetection, CopyrightValidation

admin.site.register(VideoQualityAssessment)
admin.site.register(NudityDetection)
admin.site.register(CopyrightValidation)
