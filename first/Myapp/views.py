from django.shortcuts import render
from django.http import HttpResponse
from .models import Grades,Student
# from login import models
# # Create your views here.

# # from django.shortcuts import HttpResponse

# # Create your views here.
def index(request):
    return HttpResponse('我是大帅哥')
def detail(request ,num):
    return HttpResponse('detail-%s'%num)

def grades(request):
    #去模板取数据
    gradeslist = Grades.objects.all()

    return render(request, 'Myapp/grades.html', {'grades': gradeslist})


def student(request):
    #去模板取数据
    studentlist = Student.objects.all()
 
    return render(request, 'Myapp/student.html', {'students': studentlist})

