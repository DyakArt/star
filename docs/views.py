from django.shortcuts import render
from django.http import HttpResponse


# в этом файле все функции называются либо представления, либо контроллеры
# после создания, нужно закрепить её за каким-нибудь url-адресом

def documents(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу с документами"""
    context = {
        'title': 'Документы - Отдел кадров',
        'documents_title': 'Документы'
    }
    return render(request, 'docs/documents.html', context)


def applications(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу с заявлениями"""
    context = {
        'title': 'Заявления - Отдел кадров',
        'applications_title': 'Заявления'
    }
    return render(request, 'docs/applications.html', context)
