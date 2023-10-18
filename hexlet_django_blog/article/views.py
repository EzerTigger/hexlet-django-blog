from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = 'articles'
    return render(
        request,
        'articles/index.html',
        context={'name': name}
    )
