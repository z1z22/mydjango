from django.db import models

# Create your models here.
class MeituTag(models.Model):

    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag

    class Meta:
        # abstract = True
        db_table = 'meitu_tag'  # 定义数据库表名.如果不写默认为项目名_app名

class MeituTitle(models.Model):
    titletag= models.ForeignKey("MeituTag",on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        # abstract = True
        db_table = 'meitu_title'
class MeituPic(models.Model):
    # pictag = models.ForeignKey("MeituTag",on_delete=models.CASCADE)
    pictitle = models.ForeignKey("MeituTitle",on_delete=models.CASCADE)
    picname = models.CharField(max_length=40)
    src = models.CharField(max_length=100)
    picstore = models.CharField(max_length=200)
    

    class Meta:
        db_table = 'meitu_pic'
