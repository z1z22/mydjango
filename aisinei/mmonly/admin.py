from django.contrib import admin
from .models import MmonlyTag, MmonlyTitle, MmonlyPic
# Register your models here.


@admin.register(MmonlyTag)
class MmonlyTagAdmin(admin.ModelAdmin):
    list_display = [
        'tag',
    ]
    list_per_page = 20


@admin.register(MmonlyTitle)
class MmonlyTitleAdmin(admin.ModelAdmin):
    list_display = [
        'titletag',
        'title',
    ]
    list_per_page = 20
    list_filter=['titletag']
    


@admin.register(MmonlyPic)
class MeituriPicAdmin(admin.ModelAdmin):
    list_display = [
        'pictitle',
        'picname',
        'src',
    ]
    list_per_page = 20
