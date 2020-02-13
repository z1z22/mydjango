from django.contrib import admin
from .models import MeituTag, MeituTitle, MeituPic
# Register your models here.


@admin.register(MeituTag)
class MeituTagAdmin(admin.ModelAdmin):
    list_display = [
        'tag',
    ]
    list_per_page = 20


@admin.register(MeituTitle)
class MeituTitleAdmin(admin.ModelAdmin):
    list_display = [
        'titletag',
        'title',
    ]
    list_per_page = 20
    list_filter=['titletag']
    


@admin.register(MeituPic)
class MeituPicAdmin(admin.ModelAdmin):
    list_display = [
        'pictitle',
        'picname',
        'src',
        'picstore',
    ]
    list_per_page = 20
