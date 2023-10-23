from django.shortcuts import render
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


def index(request):
    name = 'articles'
    return render(
        request,
        'articles/index.html',
        context={'name': name}
    )
