from django.apps import AppConfig


class VacanciesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vacancies'
    # меняем название группы в админ панели
    verbose_name = 'Вакансии'
