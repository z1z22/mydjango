from .models import NovohotTag, NovohotTitle, NovohotPic
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
# Create your views here.
def tag(request):
    taglist = NovohotTag.objects.all()
    return render(request, 'novohot/tag.html', {'tags':taglist})


def title(request, tagid):
    #去模板取数据
    # tag = NovohotTag.objects.get(id=tagid)
    tag = get_object_or_404(NovohotTag, id=tagid)#会运用get(),如果没有返回404
    titlelist = tag.novohottitle_set.order_by('title')
    # titlelist = NovohotTitle.objects.filter(titletag_id=tagid)#.order_by('title')
    paginator = Paginator(titlelist, 20, 4)
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
    return render(request, 'novohot/title.html', {'titles': titles})


def pic(request, tagid, titleid,):
    # piclist = MeituPic.objects.filter(pictitle_id=titleid)
    # title = NovohotTitle.objects.get(id=titleid)
    title = get_object_or_404(NovohotTitle, id=titleid)
    piclist = title.novohotpic_set.order_by('picname')

    # 实现分页功能:
    paginator = Paginator(piclist, 5, 2)
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

    return render(request, 'novohot/picture.html', {'pics':pics,'tag':tagid, 'title':title,'titleid':titleid, })

    



