from django.urls import path
from . import views
app_name='[app_name]'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<str:topic_id>/', views.topic, name='topic'),
    path('new_topics/', views.new_topic, name='new_topic'),
    path('new_topics/<str:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<str:entry_id>/', views.edit_entry, name='edit_entry'),
]