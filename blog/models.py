# coding=utf-8

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):

    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正
    body = models.TextField()
    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField()
    # 修改时间
    modified_time = models.DateTimeField()
    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    excerpt = models.CharField(max_length=200, blank=True)
    # 新增 views 字段记录阅读量
    # views = models.PositiveIntegerField(default=0)
    # 分类
    category = models.ForeignKey(Category, on_delete=False)
    # 标签
    tags = models.ManyToManyField(Tag, blank=True)
    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:reverse_article_url', kwargs={'pk': self.pk})

