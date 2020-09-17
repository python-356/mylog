from django.contrib import admin
from log.models import Category, Article
# from markdownx.widgets import AdminMarkdownxWidget
# from markdownx.admin import MarkdownxModelAdmin

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_diaplay = [
        'title',
        'author',
        'img',
        'content',
        'abstract',
        'visited',
        'category'
    ]

class CategoryAdmin(admin.ModelAdmin):
    list_diaplay = [
        'name',
    ]



# admin.site.register(Article)
# admin.site.register(Category)