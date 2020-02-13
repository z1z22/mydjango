from .models import Mm8Tag, Mm8Title, Mm8Pic
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger,InvalidPage
from django.http import HttpResponse

def tag(request):
    taglist = Mm8Tag.objects.all()
    tags = []
    for tag in taglist:
        titlesnum = tag.mm8title_set.count()
        tag_dict = {
            'tag':tag.tag,
            'num':titlesnum,
            'id':tag.id
            }
        tags.append(tag_dict)
    return render(request, 'mm8/tag.html', {'tags':tags})


def title(request, tagid):
    #去模板取数据
    tag = get_object_or_404(Mm8Tag, id=tagid)
    titlelist = tag.mm8title_set.order_by('id')
    ttlist = []
    for title in titlelist:
        pic = title.mm8pic_set.first()
        picsnum = title.mm8pic_set.count()

        title_dick = {
            'title': title.title,
            'src': pic.src,
            'id': title.id,
            'num': picsnum
        }
        ttlist.append(title_dick)

    paginator = Paginator(ttlist, 20, 4)
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
    return render(request, 'mm8/title1.html', {'titles': titles, 'tagid' :tagid, 'tag':tag})

def list_title(request, tagid):
    #去模板取数据
    tag = get_object_or_404(Mm8Tag, id=tagid)
    titlelist = tag.mm8title_set.order_by('id')
    ttlist = []
    idlist = []
    for title in titlelist:
        picsnum= title.mm8pic_set.count()
        # if picsnum == 0:
            # string = 'id={}'.format(title.id)
            # idlist.append(string)
            # idlist.append(title.id)

        title_dick = {
            'title': title.title,
            'id': title.id,
            'num': picsnum,
        }
        ttlist.append(title_dick)
    # k = ' or '.join(idlist)
    # print(k)
    # print(idlist)

    paginator = Paginator(ttlist, 20, 4)
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
    return render(request, 'mm8/title.html', {'titles': titles,  'tag':tag})

def pic(request, tagid, titleid,):
    tag = get_object_or_404(Mm8Tag, id=tagid)
    title = get_object_or_404(Mm8Title, id=titleid)
    piclist = title.mm8pic_set.order_by('picname')
    # print(request.body)
    # print('*'*80)

    # 实现分页功能:
    paginator = Paginator(piclist, 12, 4)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            pics = paginator.page(page)
        except PageNotAnInteger:
            pics = paginator.page(1)
        except InvalidPage:
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            pics = paginator.page(paginator.num_pages)

    return render(request, 'mm8/picture1.html', {'pics':pics,'tag':tag, 'title':title,})

def pic_big(request, tagid, titleid,):
    tag = get_object_or_404(Mm8Tag, id=tagid)
    title = get_object_or_404(Mm8Title, id=titleid)
    piclist = title.mm8pic_set.order_by('picname')

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

    return render(request, 'mm8/picture.html', {'pics':pics,'tag':tag, 'title':title, })
def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'mm8/error.html',{'error_msg':error_msg})
    titles = Mm8Title.objects.filter(title__icontains=q)
    number = len(titles)
    if number > 30:
        titles = titles[:30]
        error_msg = '共搜索到{}条结果,显示前30条......'.format(number,number - 30)
    

    return render(request, 'mm8/search_title.html',{'error_msg': error_msg, 'titles': titles})


# paginator

# 可选参数¶
# orphans
# 如果您不希望最后一页包含很少的项目，请使用此选项。如果最后一页通常具有小于或等于的项目数orphans，则这些项目将被添加到上一页面（成为最后一页），而不是将这些项目自己留在页面上。例如，有23个项目，per_page=10和 orphans=3，将有两个页面; 第一页有10个项目，第二页（和最后一页）有13个项目。orphans默认为零，这意味着页面永远不会合并，最后一页可能有一个项目。
# allow_empty_first_page
# 是否允许第一页为空。如果为False和 object_list空，则会引发EmptyPage错误。

# 1.类方法

# Page.has_next()  如果有下一页，则返回True。
# Page.has_previous() 如果有上一页，返回 True。
# Page.has_other_pages() 如果有上一页或下一页，返回True。
# Page.next_page_number() 返回下一页的页码。如果下一页不存在，抛出InvlidPage异常。
# Page.previous_page_number() 返回上一页的页码。如果上一页不存在，抛出InvalidPage异常。
# Page.start_index() 返回当前页上的第一个对象，相对于分页列表的所有对象的序号，从1开始。比如，将五个对象的列表分为每页两个对象，第二页的start_index()会返回3。
# Page.end_index() 返回当前页上的最后一个对象，相对于分页列表的所有对象的序号，从1开始。 比如，将五个对象的列表分为每页两个对象，第二页的end_index() 会返回 4。

# 2.类属型

# Page.object_list 当前页上所有对象的列表。
# Page.number 当前页的序号，从1开始。
# Page.paginator 相关的Paginator对象。

# 三.非法页面处理

# InvalidPage(Exception): 异常的基类，当paginator传入一个无效的页码时抛出。
# Paginator.page()放回在所请求的页面无效（比如不是一个整数）时，或者不包含任何对象时抛出异常。通常，捕获InvalidPage异常就够了，但是如果你想更加精细一些，可以捕获以下两个异常之一：

# exception PageNotAnInteger，当向page()提供一个不是整数的值时抛出。
# exception EmptyPage，当向page()提供一个有效值，但是那个页面上没有任何对象时抛出。
#        这两个异常都是InalidPage的子类，所以可以通过简单的except InvalidPage来处理它们。