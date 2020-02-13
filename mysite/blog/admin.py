from django.contrib import admin
from .models import BlogType, Blog

# Register your models here.
admin.site.register(BlogType)

admin.site.register(Blog)