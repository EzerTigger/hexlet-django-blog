from django.urls import path, reverse
from django.shortcuts import redirect

from hexlet_django_blog.article import views

urlpatterns = [
    #path('', views.IndexView.as_view()),
    path('<tags>/<int:article_id>/', views.index, name='article'),
    path('', views.index_view)
]
