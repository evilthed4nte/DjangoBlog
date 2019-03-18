from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # path('loving-shuven', views.shuven, name='shuven'),
    path('article/<int:pk>/', views.article, name='reverse_article_url'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('archives/<int:year>/<int:month>/', views.ArchivesView.as_view(), name='archives'),
    path('tag/<int:pk>/', views.TagView.as_view(), name='tag'),
]
