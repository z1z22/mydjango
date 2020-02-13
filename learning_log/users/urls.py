from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
app_name = '[app_name]'
urlpatterns = [
path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
path('logout/', views.logout_view, name='logout'),
path('register/', views.register_view, name='register'),
]