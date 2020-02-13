from django.urls import path
from . import views
app_name = '[app_name]'
urlpatterns = [
    path('', views.tag, name= "main"),
    path('<str:pictag>/', views.title, name="urltag"),
    path('<str:pictag>/<str:pictitle>/', views.pic, name="urltitle"),
]
