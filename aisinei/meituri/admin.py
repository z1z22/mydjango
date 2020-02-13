from django.contrib import admin
from .models import MeituriTag, MeituriTitle, MeituriPic
# Register your models here.


@admin.register(MeituriTag)
class MeituriTagAdmin(admin.ModelAdmin):
    list_display = [
        'tag',
    ]
    list_per_page = 20

@admin.register(MeituriTitle)
class MeituriTitleAdmin(admin.ModelAdmin):
    list_display = [
        'titletag',
        'title',
    ]
    list_per_page = 20
    list_filter=['titletag']

@admin.register(MeituriPic)
class MeituriPicAdmin(admin.ModelAdmin):
    list_display = [
        'pictitle',
        'picname',
        'src',
    ]
    list_per_page = 20
