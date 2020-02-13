from django.contrib import admin
from .models import Mm8Tag, Mm8Title, Mm8Pic
# Register your models here.


@admin.register(Mm8Tag)
class Mm8TagAdmin(admin.ModelAdmin):
    list_display = [
        'tag',
    ]
    list_per_page = 20


@admin.register(Mm8Title)
class Mm8TitleAdmin(admin.ModelAdmin):
    list_display = [
        'titletag',
        'title',
    ]
    list_per_page = 20
    list_filter=['titletag']
    


@admin.register(Mm8Pic)
class MeituriPicAdmin(admin.ModelAdmin):
    list_display = [
        'pictitle',
        'picname',
        'src',
    ]
    list_per_page = 20
