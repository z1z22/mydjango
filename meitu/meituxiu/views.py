from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#导入Paginator,EmptyPage和PageNotAnInteger模块

from .models import Meitu
from django.shortcuts import render #reditect  # 重定向

# Create your views here.


# def main(request):
#     return reditect('tag')
def tag(request):
    # itemlist = Meitu.objects.all()
    taglist = Meitu.objects.values('tag')
    # values 获得一个字典的列表,用tag.tag取值,distinct()去重
    return render(request, 'myapp/tag.html', {'tags':taglist})

def title(request,pictag):
    #去模板取数据
    titlelist = Meitu.objects.filter(tag=pictag).order_by('title').values(
        'title').distinct()#filter过滤条件,values取值,distinct()去重
    paginator = Paginator(titlelist, 20)
    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            titles = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            titles = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            titles = paginator.page(paginator.num_pages)
    return render(request, 'myapp/title.html', {'titles': titles,'pictag': pictag})


def pic(request, pictag, pictitle,):
    itemlist = Meitu.objects.filter(title=pictitle)
    # 实现分页功能:
    paginator = Paginator(itemlist, 10)
    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            pics = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            pics = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            pics = paginator.page(paginator.num_pages)

    return render(request, 'myapp/picture.html',{'tag':pictag,'title':pictitle,'pics': pics,})


'''
一、HttpRequest对象:
属性:
path:请求的完整路径
method:请求的方式,常用如:GET POST.
encoding: 浏览器提交字段的编码方式;
GET:类似字典的对象,包含GET请求包含的所有参数,如上面分页的page
POST:类似字典的对象,包含POST请求包含的所有参数
FILES:类似字典的对象,包含所有上传的文件
COOKIES:包含所有cookies的字典
session:类似字典的对象,表示当前会话
方法:
is_ajax():如果是通过XMLHttpRequest发起的会话,返回True
GET、POST的方法:
get:(如上面分页)
getlist:获取属性列表
GET属性:
POST属性:

二、HttpResponse对象:

HttpResponse方法:
1、return HttpResponse(‘数据’)直接返回数据,不调用模板;
2、render方法:
render(request, '模板路径',{需要渲染在模板上的数据})
作用是结合数据和模板,返回页面

HttpResponse属性:
content:表示返回的内容的类型;
charset:编码格式;
status_code:响应状态:响应状态码:200,304,404;
content-type:制定输出的MIME类型;

方法:
init:页面的内容实例化;
write(content):以文件的形式写入;
flush:1以文件形式输出;
set_cookies()
delete cookie

子类:
1、HttpResponseRedirect:重定向,实现页面跳转
from django.http import HttpResponse
return HttpResponseRedirect(‘要显示的重定向后的视图路径,不是模板’)
简写: reditect
from django.shortcuts import reditect


2、子类JsonResponse:返回json数据,一般用于异步情求


'''
