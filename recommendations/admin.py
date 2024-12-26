from django.contrib import admin
from .models import Recommendation 
from users.models import CustomUser  

admin.site.register(Recommendation)
