from django.shortcuts import render
from django.http import HttpResponse


# в этом файле все функции называются либо представления, либо контроллеры
# после создания, нужно закрепить её за каким-нибудь url-адресом

def vacancies(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу с вакансиями"""
    context = {
        'title': 'Вакансии - Отдел кадров',
        'vacancies_title': 'Вакансии'
    }
    return render(request, 'vacancies/vacancies.html', context)
