from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# импортируем модель новостей
from .models import News, HistoryCompany


# в этом файле все функции называются либо представления, либо контроллеры
# после создания, нужно закрепить её за каким-нибудь url-адресом


def index(request) -> HttpResponse:
    """
    Функция, которая обрабатывает запросы на главную страницу нашего сайта
    В параметр request попадает экземпляр класса http-request,
    он содержит в себе все данные о запросе (зарегистрированный пользователь или анонимный, файлы cookies,
    метод запроса (GET/POST) и тд)
    """

    # получаем все новости, начиная с актуальной
    news = News.objects.all().order_by('-id')
    # получаем запись истории компании
    history_company = HistoryCompany.objects.all().first()

    context = {
        'title': 'Отдел кадров',
        'news': news,
        'history_title': 'ИСТОРИЯ КОМПАНИИ',
        'history_company': history_company
    }
    return render(request, 'main/index.html', context)


def info(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу с полезной информацией"""
    context = {
        'title': 'Полезная информация - Отдел кадров',
        'info_title': 'Полезная информация',
        'info_content': """"""
    }
    return render(request, 'main/info.html', context)


def reserve(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу с кадровым резервом"""
    context = {
        'title': 'Кадровый резерв - Отдел кадров',
        'reserve_title': 'Кадровый резерв',
        'reserve_content': """"""
    }
    return render(request, 'main/personnel_reserve.html', context)


def policy(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу с политикой конфиденциальности"""
    context = {
        'title': 'Политика конфиденциальности - Отдел кадров',
        'policy_title': 'Политика конфиденциальности',
        'policy_content': """Текст политики конфиденциальности"""
    }
    return render(request, 'main/privacy_policy.html', context)


def hr_structure(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу со структурой отдела кадров"""
    context = {
        'title': 'Структура отдела кадров',
        'hr_title': 'Структура отдела кадров'
    }
    return render(request, 'main/hr_structure.html', context)
