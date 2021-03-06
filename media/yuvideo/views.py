from .models import YuvideoTag, YuvideoVideo
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger,InvalidPage
from django.http import HttpResponse

def tag(request):
    taglist = YuvideoTag.objects.all()
    return render(request, 'yuvideo/tag.html', {'tags':taglist})


def title(request, tagid):
    #去模板取数据
    tag = get_object_or_404(YuvideoTag, id=tagid)
    titlelist = tag.yuvideovideo_set.order_by('-id')


    paginator = Paginator(titlelist, 12, 4)
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
    return render(request, 'yuvideo/title.html', {'titles': titles, 'tag':tag})


def video(request, tagid, videoid,):
    tag = get_object_or_404(YuvideoTag, id=tagid)
    video = get_object_or_404(YuvideoVideo, id=videoid)
    # video.mp4href = video.mp4href.replace('.gif','')

    return render(request, 'yuvideo/video.html', {'video':video,'tag':tag})

def search(request):
    q = request.GET.get('q')
    print(q)
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'yuvideo/error.html',{'error_msg':error_msg})
    videoname = YuvideoVideo.objects.filter(videoname__icontains=q)
    number = len(videoname)
    if number > 30:
        tivideonametles = videoname[:30]
        error_msg = '共搜索到{}条结果,显示前30条......'.format(number)
    

    return render(request, 'yuvideo/search_title.html',{'error_msg': error_msg, 'titles': videoname})