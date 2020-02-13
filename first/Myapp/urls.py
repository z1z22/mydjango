from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('<int:num>/', views.detail),
    path('grades/', views.grades),
    path('student/', views.student),
]
#int任何正整数
#str 除路径分隔符外的任何非空字符串
#slug 匹配有ASCII编码的任何slug字符串,以及连接符号,如ding-dang-huo-1st
#uuid 如34343442-432432-4321-43-43-43
#path 匹配包括‘/’的完整路径
