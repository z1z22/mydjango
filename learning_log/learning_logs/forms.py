
from django import forms
from .models import Topic, Entry
'''创建表单的最简单方式是使用ModelForm，它根据我们在第18章定义的模型中的信息自动创建表单。'''
class TopicForm(forms.ModelForm):   
    class Meta:
        model = Topic
        fields = ("text",)
        labels = {"text": ""}

class EntryForm(forms.ModelForm):
    
    class Meta:
        model = Entry
        fields = ("text",)
        labels = {"text":""}
        Widgets={'text':forms.Textarea(attrs={'cols':80})}
