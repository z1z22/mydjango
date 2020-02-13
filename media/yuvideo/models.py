from django.db import models

# Create your models here.
class YuvideoTag(models.Model):

    tag = models.CharField(max_length=20)
    def __str__(self):
        return self.tag
        
    class Meta:
        db_table = 'yuvideo_tag'  # 定义数据库表名.如果不写默认为项目名

    
class YuvideoVideo(models.Model):
    videotag = models.ForeignKey("YuvideoTag",on_delete=models.CASCADE)
    videoname = models.CharField(max_length=100)
    src = models.URLField(max_length=100)
    mp4href = models.URLField(max_length=100)


    class Meta:
        db_table = 'yuvideo_video'
