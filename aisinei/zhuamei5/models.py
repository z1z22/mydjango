from django.db import models

# Create your models here.
class Zhuamei5Tag(models.Model):

    tag = models.CharField(max_length=20)
    def __str__(self):
        return self.tag
        
    class Meta:
        db_table = 'zhuamei5_tag'  # 定义数据库表名.如果不写默认为项目名_app名

class Zhuamei5Title(models.Model):
    titletag= models.ForeignKey("Zhuamei5Tag",on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'zhuamei5_title'
        
class Zhuamei5Pic(models.Model):
    pictitle = models.ForeignKey("Zhuamei5Title",on_delete=models.CASCADE)
    picname = models.CharField(max_length=50)
    src = models.URLField(max_length=100)
    

    class Meta:
        db_table = 'zhuamei5_pic'


