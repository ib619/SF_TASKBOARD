from django.contrib import admin
from .models import Article, Response
from .forms import ArticleForm, ResponseForm


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ['author']
    form = ArticleForm


admin.site.register(Article, ArticleAdmin)


class ResponseAdmin(admin.ModelAdmin):
    readonly_fields = ['author', 'article']
    form = ResponseForm


admin.site.register(Response, ResponseAdmin)
