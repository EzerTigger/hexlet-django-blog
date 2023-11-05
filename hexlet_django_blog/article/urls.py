from django.urls import path, reverse
from django.shortcuts import redirect

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles'),
    path('<tags>/<int:article_id>/', views.index, name='article'),
    path('<int:id>/edit/', views.ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/', views.ArticleView.as_view(), name='show_article'),
    path('create/', views.ArticleFormCreateView.as_view(), name='articles_create'),
]
