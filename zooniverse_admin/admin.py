from django.contrib import admin
from .models import AnimalClassification, PlanktonClassification, SubjectGroup, ProjectRecommendation

admin.site.register(AnimalClassification)
admin.site.register(PlanktonClassification)
admin.site.register(SubjectGroup)
admin.site.register(ProjectRecommendation)
