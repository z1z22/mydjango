from django.db import models
# Create your models here.

class Grades(models.Model):

    gname = models.CharField(max_length=20, verbose_name='班级名称')
    gdate = models.DateField(auto_now=False, auto_now_add=False,verbose_name='年 份')
    ggirlnum = models.IntegerField(verbose_name='女生人数')
    gboynum = models.IntegerField(verbose_name='男生人数')
    isDelete = models.BooleanField(default=False,verbose_name='已删除')
    def __str__(self):
        return self.gname
    


class Student(models.Model):
    GENDER_CHOICES = (('男','男'),('女','女'),)
    # choices = GENDER_CHOICES,
    sname = models.CharField(max_length=20, verbose_name='姓  名')
    sgender = models.CharField(
        max_length=30, verbose_name='性  别', choices=GENDER_CHOICES)
    sage = models.IntegerField(verbose_name='年  龄')
    scontent = models.CharField(max_length=20, verbose_name='简  介')
    isDelete = models.BooleanField(default=False, verbose_name='已删除')
    sgrade = models.ForeignKey(Grades, on_delete=models.CASCADE, verbose_name='班 级')
    def __str__(self):
        return self.sname
    #自定义模型管理器,如果不定义django自动创建名为objects
    # stuObj= models.Manage()
    class Meta:
        db_table = 'students'#定义数据库表名.如果不写默认为项目名_app名
        ordering = ['id']#按照规定的字段排序
        ordering = ['-id']#降序前面加减号

    

    # CASCADE
