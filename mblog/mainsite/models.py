from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    #title用来显示文章标题
    title = models.CharField(max_length=200)
    #slug用来显示文章网址
    slug = models.CharField(max_length=200)
    #用来显示文章内容
    body = models.TextField()
    #pub_date用来显示文章发表的时间
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title
