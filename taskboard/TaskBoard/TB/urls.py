from django.urls import path
from .views import ArticleList, ArticleCreateView, ArticleDetail, ArticleUpdateView, ArticleDeleteView
from .views import ResponseCreateView, ResponseList, ResponseUpdateView

urlpatterns = [
    path('', ArticleList.as_view(), name='articles'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('detail/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='article_delete'),
    path('respond/', ResponseCreateView.as_view(), name='respond'),
    path('responses/', ResponseList.as_view(), name='responses'),
    path('decide/<int:pk>', ResponseUpdateView.as_view(), name='decide'),
]