from django.contrib import admin
from .models import NovohotTag, NovohotTitle, NovohotPic
# Register your models here.


@admin.register(NovohotTag)
class NovohotTagAdmin(admin.ModelAdmin):
    list_display = [
        'tag',
    ]
    list_per_page = 10


@admin.register(NovohotTitle)
class NovohotTitleAdmin(admin.ModelAdmin):
    list_display = [
        'titletag',
        'title',
    ]
    list_per_page = 10
    list_filter=['titletag']
    


@admin.register(NovohotPic)
class NovohotPicAdmin(admin.ModelAdmin):
    list_display = [
        'pictitle',
        'picname',
        'src',
        'picstore',
    ]
    list_per_page = 10
