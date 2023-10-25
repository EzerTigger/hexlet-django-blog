from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import View


class IndexView(View):
    name = 'articles'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'articles/index.html',
            context={'name': self.name}
        )


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
