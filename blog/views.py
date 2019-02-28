from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Article
import markdown


def index(request):
    article_list = Article.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'article_list': article_list
    })


# 文章详情
def article(request, pk):
    article_detail = get_object_or_404(Article, pk=pk)
    article_detail.body = markdown.markdown(article_detail.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    return render(request, 'blog/detail.html', context={
        'article_detail': article_detail
    })
