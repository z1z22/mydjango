from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=30)

    # class Meta:
    #     verbose_name = _("BlogType")
    #     verbose_name_plural = _("BlogTypes")

    def __str__(self):
        return self.type_name

    # def get_absolute_url(self):
    #     return reverse("BlogType_detail", kwargs={"pk": self.pk})

class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = models.TextField()
    authr = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)
    last_updata_time = models.DateTimeField(auto_now=True)

    # class Meta:
    #     verbose_name = _("Blog")
    #     verbose_name_plural = _("Blogs")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Blog_detail", kwargs={"pk": self.pk})




