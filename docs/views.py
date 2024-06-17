from django.shortcuts import render
from django.http import HttpResponse

# импортируем модели
from .models import Documents, Applications
from .utils import q_search


# в этом файле все функции называются либо представления, либо контроллеры
# после создания, нужно закрепить её за каким-нибудь url-адресом

def documents(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу с документами"""

    docs = Documents.objects.all()
    query = request.GET.get('q', None)

    # если поисковый запрос
    if query:
        docs = q_search(query, docs=docs)

    context = {
        'title': 'Документы - Отдел кадров',
        'documents_title': 'Документы',
        'docs': docs
    }
    return render(request, 'docs/documents.html', context)


def applications(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу с заявлениями"""

    apps = Applications.objects.all()
    query = request.GET.get('q', None)

    # если поисковый запрос
    if query:
        apps = q_search(query, apps=apps)

    context = {
        'title': 'Заявления - Отдел кадров',
        'applications_title': 'Заявления',
        'apps': apps
    }
    return render(request, 'docs/applications.html', context)
