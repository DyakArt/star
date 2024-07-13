from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from django.shortcuts import redirect

# импортируем модели
from .models import VacanciesGroup, Vacancies, FilesVacanciesGroup, VacFiles
# импортируем форму для отклика на вакансию
from .forms import JobResponseForm

# импортируем модули для работы с почтой
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# в этом файле все функции называются либо представления, либо контроллеры
# после создания, нужно закрепить её за каким-нибудь url-адресом

def vacancies(request) -> HttpResponse:
    """Функция, которая обрабатывает запросы на страницу с вакансиями"""
    if request.method == 'POST':
        form = JobResponseForm(data=request.POST)
        if form.is_valid():
            data = {
                'job_title': form.cleaned_data['job_title'],
                'full_name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
            }
            # передаем данные в шаблон для отправки на почту
            html_body = render_to_string('email/email.html', data)
            # формируем сообщение для почты
            msg = EmailMultiAlternatives(subject='Отклик на вакансию', to=['dyakovich.artyom@yandex.ru'])
            msg.attach_alternative(html_body, 'text/html')
            msg.send()

            messages.success(request, 'Ваш отклик отправлен!')
            return redirect('vacancies:vacancies')
    else:
        form = JobResponseForm()

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

    context = {
        'title': 'Вакансии - Отдел кадров',
        'vacancies_title': 'Вакансии',
        'group_vac': group_vac,
        'group_vac_files': group_vac_files,
        'form': form
    }
    return render(request, 'vacancies/vacancies.html', context)
