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