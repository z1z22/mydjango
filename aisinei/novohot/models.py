from django.db import models

# Create your models here.
class NovohotTag(models.Model):

    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag

    class Meta:
        # abstract = True
        db_table = 'novohot_tag'  # 定义数据库表名.如果不写默认为项目名_app名

class NovohotTitle(models.Model):
    titletag= models.ForeignKey("NovohotTag",on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        # abstract = True
        db_table = 'novohot_title'
class NovohotPic(models.Model):
    # pictag = models.ForeignKey("MeituTag",on_delete=models.CASCADE)
    pictitle = models.ForeignKey("NovohotTitle",on_delete=models.CASCADE)
    picname = models.CharField(max_length=100)
    src = models.CharField(max_length=200)
    picstore = models.CharField(max_length=300)
    

    class Meta:
        db_table = 'novohot_pic'
