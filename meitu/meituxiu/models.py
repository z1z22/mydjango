from django.db import models

# Create your models here.
class Meitu(models.Model):
    title = models.CharField( max_length=100)
    picname = models.CharField( max_length=40)
    tag = models.CharField(max_length=20)
    src = models.CharField(max_length=100)
    picstore = models.CharField(max_length=200)

    # class Meta:
        # db_table = 'meitupic'  # 定义数据库表名.如果不写默认为项目名_app名

    def __str__(self):
        return self.title + '_' + self.picname
#如果模型类没有指定管理器,软件自动为模型创建一个名字为object的管理器
#可以自定义管理器,自定义后objects就不存在了:
    # meituObj = models.Manager()
    # meituObj = PicManager()
#还可以自定义管理器类,一个模型类可以有多个模型管理器:
# class PicManager(modles.Manager):
#     def get_queryset(self):
#         return super(PicManager,self).get_queryset().filter(title = '')#过滤按照条件

# 创建对象,主要为了向数据库存数据:
# @classmethod#类方法
# def createpic(cls, title, picname, tag,src,picstore):

