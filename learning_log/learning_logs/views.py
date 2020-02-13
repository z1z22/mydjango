from django.shortcuts import render
from .models import Topic, Entry

#为用户输入表单引入表单模块
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html',context)


@login_required
def topic(request,topic_id):
    context = {}
    context['topic'] = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    if context['topic'].owner != request.user: 
        raise Http404
    context['entries'] = context['topic'].entry_set.order_by('-date_added')
    # context = {'topic':topic,'entries':entries}
    return render(request, 'learning_logs/topic.html',context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False) 
            new_topic.owner = request.user 
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request,'learning_logs/new_topic.html', context)


@login_required
def new_entry(request,topic_id):
    context = {}
    context['topic'] = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        context['form'] = EntryForm()
    else:
        context['form'] = EntryForm(data=request.POST)
        if context['form'].is_valid():
            new_entry = context['form'].save(commit=False)
            new_entry.topic = context['topic'] 
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    # context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request,entry_id):
    context = {}
    context['entry'] = Entry.objects.get(id=entry_id)
    context['topic'] = context['entry'].topic
    # 确认请求的主题属于当前用户
    if context['topic'].owner != request.user: 
        raise Http404
    if request.method != 'POST':
        context['form'] = EntryForm(instance=context['entry'])
    else:
        context['form'] = EntryForm(instance=context['entry'],data=request.POST)
        if context['form'].is_valid():
            context['form'].save()
            return HttpResponseRedirect(
                reverse('learning_logs:topic', args=[topic.id]))
    # context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
