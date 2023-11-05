from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib import messages

from hexlet_django_blog.article.forms import ArticleForm
from hexlet_django_blog.article.models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья добавлена успешно')
            return redirect('articles')

        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {
            'form': form,
            'article_id': article_id
        })

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья успешно изменена')
            return redirect('articles')

        return render(request, 'articles/update.html',
                      {'form': form, 'article_id': article_id})


def index(request, tags, article_id):
    return render(
        request,
        'articles/index.html',
        context={'tags': tags, 'article_id': article_id}
    )


def index_view(request):
    return redirect(reverse('article', kwargs={
        'tags': 'python',
        'article_id': 42
    }))
