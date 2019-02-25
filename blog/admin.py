from django.contrib import admin
from blog.models import Article, Tag, Category

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)
