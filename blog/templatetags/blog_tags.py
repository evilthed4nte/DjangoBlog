from django import template
from django.db.models import Count
from django.views.generic import ListView

from ..models import Article, Category, Tag


def get_recent_article(num=5):
    return Article.objects.all().order_by('-created_time')[:num]


register = template.Library()


@register.simple_tag
def get_recent_article(num=5):
    return Article.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Article.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # return Category.objects.all()
    return Category.objects.annotate(num_article=Count('article')).filter(num_article__gt=0)


@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_article=Count('article')).filter(num_article__gt=0)

