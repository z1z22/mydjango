from .models import MeituTag, MeituTitle, MeituPic
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger,InvalidPage
from django.http import HttpResponse

# Create your views here.

def tag(request):
    taglist = MeituTag.objects.all()
    return render(request, 'meituxiu/tag.html', {'tags':taglist})


def title(request, tagid):
    #去模板取数据
    # tag = MeituTag.objects.get(id=tagid )
    tag = get_object_or_404(MeituTag, pk=tagid)
    titlelist = tag.meitutitle_set.all()#order_by('title')
    ttlist = []
    for title in titlelist:
        # print(title.id)
        pic = title.meitupic_set.order_by('picname')[0]
        # pic = MeituPic.objects.get( pictitle=title.id)
        # print(pic.src)
        adick = {
            'title': title.title,
            'src': pic.src,
            'id': title.id
        }
        ttlist.append(adick)

    # titlelist = MeituTitle.objects.filter(titletag_id=tagid)#.order_by('title')
    paginator = Paginator(ttlist, 20, 4)
    # paginator = Paginator(titlelist, 20)
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
    return render(request, 'meituxiu/title1.html', {'titles': titles, 'tagid' :tagid, 'tag':tag})


def pic(request, tagid, titleid,):
    # piclist = MeituPic.objects.filter(pictitle_id=titleid)
    # title = MeituTitle.objects.get(id=titleid)
    title = get_object_or_404(MeituTitle, pk=titleid)
    piclist = title.meitupic_set.all()#.order_by('picname')
    print(request.body)
    print('*'*80)

    # 实现分页功能:
    paginator = Paginator(piclist, 12, 4)
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

    return render(request, 'meituxiu/picture1.html', {'pics':pics,'tag':tagid, 'title':title,'titleid':titleid, })

def pic_big(request, tagid, titleid,):

    title = get_object_or_404(MeituTitle, pk=titleid)
    piclist = title.meitupic_set.all()#.order_by('picname')

    # 实现分页功能:
    paginator = Paginator(piclist, 12, 4)
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

    return render(request, 'meituxiu/picture.html', {'pics':pics,'tag':tagid, 'title':title,'titleid':titleid, })

def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'meituxiu/error.html',{'error_msg':error_msg})
    titles = MeituTitle.objects.filter(title__icontains=q)
    number = len(titles)
    if number > 30:
        titles = titles[:30]
        error_msg = '共搜索到{}条结果,还有{}条结果未显示......'.format(number,number - 30)
 
    return render(request, 'meituxiu/search_title.html', {'error_msg': error_msg, 'titles': titles})
