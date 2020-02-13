from django.urls import path
from . import views
app_name = '[app_name]'
urlpatterns = [
    path('', views.tag,name='main' ),
    path('<int:tagid>/', views.title, name="urltitle"),
    path('<int:tagid>/<int:videoid>/', views.video, name="video"),

]