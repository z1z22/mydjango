from django.urls import path
from . import views
app_name = '[app_name]'
urlpatterns = [
    path('', views.tag,name='main' ),
    path('<int:tagid>/', views.title, name="urltag"),
    path('<int:tagid>list/', views.list_title, name="list_title"),
    path('<int:tagid>/<int:titleid>/', views.pic, name="urltitle"),
    path('<int:tagid>/<int:titleid>/big', views.pic_big, name="urlpicbig"),
    path('search/', views.search, name="search"),

]

# 命名正则表达式组的语法是(?P<name>pattern)，
# re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
# 除了命名组语法之外，例如(?P<year>[0-9]{4})，您还可以使用较短的未命名组，例如([0-9]{4})。



