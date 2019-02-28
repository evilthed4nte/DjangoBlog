from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from blog.models import Article, Category, Tag


# def index(request):
#     article_list = Article.objects.all().order_by('-created_time')
#     return render(request, 'blog/index.html', context={
#         'article_list': article_list
#     })
# 类视图
class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article_list'


# 分类详情页
class CategoryView(ListView):
    model = Category
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


# 归档页
class ArchivesView(ListView):
    archives = Article.objects.dates('created_time', 'month', order='DESC')
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                               created_time__month=month)


# 标签页
class TagView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)


# 文章详情
def article(request, pk):
    article_detail = get_object_or_404(Article, pk=pk)
    import markdown
    article_detail.body = markdown.markdown(article_detail.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    return render(request, 'blog/detail.html', context={
        'article_detail': article_detail
    })


# TODO
# 详情页类视图class AriticleView(DetailView):
