import uuid
import os
import re

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.

# from markdownx.models import MarkdownxField
# from markdownx.utils import markdownify
# from taggit.managers import TaggableManager


def article_img_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    # filename = '{}.{}'.format(uuid.uuid4().hex[:8],ext)
    return os.path.join("avatar", filename)


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='类别名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField(verbose_name="文章标题", max_length=50)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    img = models.ImageField(upload_to=article_img_path, null=True, blank=True, verbose_name="文章配图")
    content = models.TextField(verbose_name='文章内容')
    # content = MarkdownxField(verbose_name='文章内容')
    abstract = models.TextField(verbose_name='文章摘要', null=True, blank=True, max_length=255)
    visited = models.PositiveIntegerField(verbose_name="访问量", default=0)
    category = models.ManyToManyField('Category', verbose_name='文章分类')
    # tags = models.ManyToManyField('Tag', verbose_name='文章标签')
    # tags = TaggableManager(verbose_name='文章标签')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客内容'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def get_absolute_url(self):
        """
        获取当前详情页的url(反向解析)
        return: 详情页url地址
        """
        return reverse("blog:blog_detail", kwargs={'detail_id': self.id})  # reverse适用于 FBV

    def increase_visited(self):
        """
        访问量 +1
        """
        self.visited += 1
        self.save(update_fields=['visited'])

    # def get_markdown(self):
    #     """
    #     将 markdown文本转为 html
    #     """
    #     return markdownify(self.content)


