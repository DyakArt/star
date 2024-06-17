from django.contrib import admin
from main.admin import CheckCountRecordsInTables

# импортируем таблицы из models
from .models import VacanciesGroup, Vacancies, VacFiles, FilesVacanciesGroup

# регистрируем таблицу VacanciesGroup в админ панели
admin.site.register(VacanciesGroup)

# регистрируем таблицу Vacancies в админ панели
admin.site.register(Vacancies)

# регистрируем таблицу VacFiles в админ панели
admin.site.register(VacFiles)

# регистрируем таблицу FilesVacanciesGroup в админ панели
admin.site.register(FilesVacanciesGroup)
