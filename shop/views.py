from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse('Page shop apps')


def categories(request, catid):
    return HttpResponse(f'Page categories {catid}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')