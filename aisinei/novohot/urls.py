from django.urls import path
from . import views
app_name = '[app_name]'
urlpatterns = [
    path('', views.tag,name='main' ),
    path('<int:tagid>/', views.title, name="urltag"),
    path('<int:tagid>/<int:titleid>/', views.pic, name="urltitle"),
]