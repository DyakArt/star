from django.db import models


class VacanciesGroup(models.Model):
    """Таблица для групп вакансий"""
    # Поле для названия группы вакансий
    group_title = models.CharField(max_length=70, verbose_name='Название раздела')

    # создаем класс, чтобы поменять некоторые данные (например, название таблицы в БД, в админ панели)
    class Meta:
        # обычно таблицы называют в единственном числе (здесь, как она будет отображаться в БД)
        db_table = 'vacancies_group'
        # как будет отображаться в админ панели (в единственном числе)
        verbose_name = 'Раздел вакансий'
        # в множественном числе
        verbose_name_plural = 'Разделы вакансий'

    # метод перегрузки для вывода объекта (изменяем отображение каждой группы вакансий в админ панели)
    def __str__(self):
        return self.group_title


class Vacancies(models.Model):
    """Таблица для вакансий"""
    # Поле для названия должности
    job_title = models.CharField(max_length=200, verbose_name='Название должности')
    # Поле для названия подразделения
    subunit = models.CharField(max_length=70, verbose_name='Название подразделения', blank=True, null=True)
    # Поле для требуемого образования
    required_education = models.CharField(max_length=200, verbose_name='Требуемое образование', blank=True, null=True)
    # Поле для номера телефона
    phone = models.CharField(max_length=50, verbose_name='Телефон', blank=True, null=True)
    # Поле для зарплаты
    salary = models.CharField(max_length=6, verbose_name='Зарплата', blank=True, null=True)
    # получаем (связываем) таблицу VacanciesGroup (внешний ключ)
    vacancies_group = models.ForeignKey(to=VacanciesGroup, on_delete=models.CASCADE, verbose_name='Раздел вакансий',
                                        related_name='vacancies')

    # создаем класс, чтобы поменять некоторые данные (например, название таблицы в БД, в админ панели)
    class Meta:
        # обычно таблицы называют в единственном числе (здесь, как она будет отображаться в БД)
        db_table = 'vacancies'
        # как будет отображаться в админ панели (в единственном числе)
        verbose_name = 'Вакансию'
        # в множественном числе
        verbose_name_plural = 'Вакансии'

    # метод перегрузки для вывода объекта (изменяем отображение должности каждой вакансии в админ панели)
    def __str__(self):
        return self.job_title


class FilesVacanciesGroup(models.Model):
    """Таблица для разделов файлов в вакансиях"""
    # Поле для названия группы вакансий
    group_file_title = models.CharField(max_length=70, verbose_name='Название раздела файлов')

    class Meta:
        # обычно таблицы называют в единственном числе (здесь, как она будет отображаться в БД)
        db_table = 'files_vacancies_group'
        # как будет отображаться в админ панели (в единственном числе)
        verbose_name = 'Раздел файлов'
        # в множественном числе
        verbose_name_plural = 'Разделы с файлами'

    # метод перегрузки для вывода объекта (изменяем отображение каждой группы файлов вакансий в админ панели)
    def __str__(self):
        return self.group_file_title


class VacFiles(models.Model):
    """Таблица для файлов вакансий"""
    # Поле для названия файла
    file_name = models.CharField(max_length=255, verbose_name='Название файла', default='Скачать бланк', blank=True, null=True)
    # Поле для файла вакансии
    file_vac = models.FileField(upload_to='documents/vacancies/', verbose_name='Файл для раздела вакансий', blank=True,
                                null=True)
    # получаем (связываем) таблицу VacanciesGroup (внешний ключ)
    vac_files_group = models.ForeignKey(to=FilesVacanciesGroup, on_delete=models.CASCADE,
                                        verbose_name='Раздел файлов вакансий',
                                        related_name='vac_files')

    # создаем класс, чтобы поменять некоторые данные (например, название таблицы в БД, в админ панели)
    class Meta:
        # обычно таблицы называют в единственном числе (здесь, как она будет отображаться в БД)
        db_table = 'vac_files'
        # как будет отображаться в админ панели (в единственном числе)
        verbose_name = 'Файл'
        # в множественном числе
        verbose_name_plural = 'Файлы'

    # метод перегрузки для вывода объекта (изменяем отображение названия для каждого файла раздела вакансий в админ панели)
    def __str__(self):
        return self.file_vac.name.split('/')[-1]
