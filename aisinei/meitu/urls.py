"""meitu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meitulu/', include('meituxiu.urls', namespace = 'meitu',)),
    path('novohot/', include('novohot.urls', namespace = 'novohot',)),
    path('meituri/', include('meituri.urls', namespace = 'meituri',)),
    path('mmonly/', include('mmonly.urls', namespace = 'mmonly',)),
    path('mm8/', include('mm8.urls', namespace = 'mm8',)),
    path('zhuamei5/', include('zhuamei5.urls', namespace = 'zhuamei5',)),
]