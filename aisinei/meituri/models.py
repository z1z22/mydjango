from django.db import models

# Create your models here.
class MeituriTag(models.Model):

    tag = models.CharField(max_length=20)
    def __str__(self):
        return self.tag
        
    class Meta:
        db_table = 'meituri_tag'  # 定义数据库表名.如果不写默认为项目名_app名

class MeituriTitle(models.Model):
    titletag= models.ForeignKey("MeituriTag",on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'meituri_title'
        
class MeituriPic(models.Model):
    pictitle = models.ForeignKey("MeituriTitle",on_delete=models.CASCADE)
    picname = models.CharField(max_length=200)
    # src = models.CharField(max_length=100)
    src = models.URLField(max_length=100)
    # picstore = models.CharField(max_length=200)
    

    class Meta:
        db_table = 'meituri_pic'


