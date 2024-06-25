from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages

# импортируем модели
from .models import VacanciesGroup, Vacancies, FilesVacanciesGroup, VacFiles


# в этом файле все функции называются либо представления, либо контроллеры
# после создания, нужно закрепить её за каким-нибудь url-адресом

def vacancies(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу с вакансиями"""

    vac = Vacancies.objects.all()
    groups = VacanciesGroup.objects.all()

    vac_files = VacFiles.objects.all()
    vac_files_groups = FilesVacanciesGroup.objects.all()

    group_vac = {}
    group_vac_files = {}

    for group in groups:
        vacs = group.vacancies.all()
        group_vac[group.group_title] = vacs

    for group in vac_files_groups:
        files = group.vac_files.all()
        group_vac_files[group.group_file_title] = files

    # получаем параметр accept_policy
    accept_policy = request.GET.get('accept_policy', None)

    context = {
        'title': 'Вакансии - Отдел кадров',
        'vacancies_title': 'Вакансии',
        'group_vac': group_vac,
        'group_vac_files': group_vac_files
    }
    return render(request, 'vacancies/vacancies.html', context)
