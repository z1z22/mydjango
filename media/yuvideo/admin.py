from django.contrib import admin
from .models import YuvideoTag, YuvideoVideo
# Register your models here.

@admin.register(YuvideoTag)
class MmonlyTagAdmin(admin.ModelAdmin):
    list_display = [
        'tag',
    ]
    list_per_page = 20


# @admin.register(Yuvideotitle)
# class MmonlyTitleAdmin(admin.ModelAdmin):
#     list_display = [
#         'titletag',
#         'title',
#     ]
#     list_per_page = 20
#     list_filter=['titletag']
    

@admin.register(YuvideoVideo)
class MeituriPicAdmin(admin.ModelAdmin):
    list_display = [
        'videotag',
        'videoname',
        'src',
        'mp4href',
    ]
    list_per_page = 20
