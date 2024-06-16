from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.models import Group
# импортируем модели
from .models import News, HistoryCompany, Reserve, Info, Policy, UserProfile


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


def reserve(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу с кадровым резервом"""

    reserve_content = Reserve.objects.all().first()

    context = {
        'title': 'Кадровый резерв - Отдел кадров',
        'reserve_title': 'Кадровый резерв',
        'reserve_content': reserve_content
    }
    return render(request, 'main/personnel_reserve.html', context)


def info(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу с полезной информацией"""

    info_content = Info.objects.all().first()

    context = {
        'title': 'Полезная информация - Отдел кадров',
        'info_title': 'Полезная информация',
        'info_content': info_content
    }
    return render(request, 'main/info.html', context)


def policy(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу с политикой конфиденциальности"""

    policy_content = Policy.objects.all().first()

    context = {
        'title': 'Политика конфиденциальности - Отдел кадров',
        'policy_title': 'Политика конфиденциальности',
        'policy_content': policy_content
    }
    return render(request, 'main/privacy_policy.html', context)


def hr_structure(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу со структурой отдела кадров"""

    user = UserProfile.objects.all()
    groups = Group.objects.all()

    group_users = {}

    for group in groups:
        users = group.user_set.all()
        group_users[group.name] = users

    context = {
        'title': 'Структура отдела кадров',
        'hr_title': 'Структура отдела кадров',
        'group_users': group_users
    }
    return render(request, 'main/hr_structure.html', context)
