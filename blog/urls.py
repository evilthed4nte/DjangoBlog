from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('article/<int:pk>/', views.article, name='reverse_article_url'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('tag/<int:pk>/', views.TagView.as_view(), name='tag'),
    path('archives/<int:year>/<int:month>/', views.ArchivesView.as_view(), name='archives')


    # url(r'^$', views.index, name='show_index'),
    # url(r'^article/(?P<pk>[0-9]+)/$', views.article, name='detail'),
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    # url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    # url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
]
