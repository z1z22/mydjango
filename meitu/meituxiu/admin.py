from django.contrib import admin
from .models import Meitu
# Register your models here.
@admin.register(Meitu)
class MeituAdmin(admin.ModelAdmin):
    list_display = [
        'tag',
        'title',
        'picname',
        'src',
    ]
    list_filter = ['tag']
    list_per_page = 20
