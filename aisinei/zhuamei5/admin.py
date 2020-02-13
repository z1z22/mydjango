from django.contrib import admin
from .models import Zhuamei5Tag, Zhuamei5Title, Zhuamei5Pic
# Register your models here.


@admin.register(Zhuamei5Tag)
class Zhuamei5TagAdmin(admin.ModelAdmin):
    list_display = [
        'tag',
    ]
    list_per_page = 20


@admin.register(Zhuamei5Title)
class Zhuamei5TitleAdmin(admin.ModelAdmin):
    list_display = [
        'titletag',
        'title',
    ]
    list_per_page = 20
    list_filter=['titletag']
    


@admin.register(Zhuamei5Pic)
class Zhuamei5PicAdmin(admin.ModelAdmin):
    list_display = [
        'pictitle',
        'picname',
        'src',
    ]
    list_per_page = 20
