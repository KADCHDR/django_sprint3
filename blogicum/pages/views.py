from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def about(request: HttpRequest) -> HttpResponse:
    """Отображает страницу 'О сайте'."""
    template_name = 'pages/about.html'
    return render(request, template_name)


def rules(request: HttpRequest) -> HttpResponse:
    """Отображает страницу с правилами сайта."""
    template_name = 'pages/rules.html'
    return render(request, template_name)
