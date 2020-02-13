from django.db import models

# Create your models here.
class Mm8Tag(models.Model):

    tag = models.CharField(max_length=20)
    def __str__(self):
        return self.tag
        
    class Meta:
        db_table = 'mm8_tag'  # 定义数据库表名.如果不写默认为项目名_app名

class Mm8Title(models.Model):
    titletag= models.ForeignKey("Mm8Tag",on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'mm8_title'
        
class Mm8Pic(models.Model):
    pictitle = models.ForeignKey("Mm8Title",on_delete=models.CASCADE)
    picname = models.CharField(max_length=50)
    src = models.URLField(max_length=100)
    

    class Meta:
        db_table = 'mm8_pic'


