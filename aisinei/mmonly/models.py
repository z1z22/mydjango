from django.db import models

# Create your models here.
class MmonlyTag(models.Model):

    tag = models.CharField(max_length=20)
    def __str__(self):
        return self.tag
        
    class Meta:
        db_table = 'mmonly_tag'  # 定义数据库表名.如果不写默认为项目名_app名

class MmonlyTitle(models.Model):
    titletag= models.ForeignKey("MmonlyTag",on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'mmonly_title'
        
class MmonlyPic(models.Model):
    pictitle = models.ForeignKey("MmonlyTitle",on_delete=models.CASCADE)
    picname = models.CharField(max_length=50)
    src = models.URLField(max_length=100)
    

    class Meta:
        db_table = 'mmonly_pic'


