from django.db import models


# Через эти классы мы также можем взаимодействовать с таблицами из БД.
# Создаем таблицу для документов
class Documents(models.Model):
    # Поле для названия документа
    name_document = models.CharField(max_length=255, verbose_name='Название документа', blank=True, null=True)
    # Поле для загрузки документа
    file_doc = models.FileField(upload_to='documents/', verbose_name='Документ')

    # создаем класс, чтобы поменять некоторые данные (например, название таблицы в БД, в админ панели)
    class Meta:
        # обычно таблицы называют в единственном числе (здесь, как она будет отображаться в БД)
        db_table = 'documents'
        # как будет отображаться в админ панели (в единственном числе)
        verbose_name = 'Документ'
        # в множественном числе
        verbose_name_plural = 'Документы'

    def save(self, *args, **kwargs):
        # Если название документа не задано, используем имя файла
        if not self.name_document:
            self.name_document = self.file_doc.name.split('/')[-1]
        super(Documents, self).save(*args, **kwargs)

    # метод перегрузки для вывода объекта (изменяем отображение заголовка каждого документа в админ панели)
    def __str__(self):
        return self.name_document


# Создаем таблицу для заявлений
class Applications(models.Model):
    # Поле для названия заявления
    name = models.CharField(max_length=255, verbose_name='Название заявления', blank=True, null=True)
    # Поле для загрузки заявления
    file_app = models.FileField(upload_to='documents/applications/', verbose_name='Заявление')

    # создаем класс, чтобы поменять некоторые данные (например, название таблицы в БД, в админ панели)
    class Meta:
        # обычно таблицы называют в единственном числе (здесь, как она будет отображаться в БД)
        db_table = 'applications'
        # как будет отображаться в админ панели (в единственном числе)
        verbose_name = 'Заявление'
        # в множественном числе
        verbose_name_plural = 'Заявления'

    def save(self, *args, **kwargs):
        # Если название заявления не задано, используем имя файла
        if not self.name:
            self.name = self.file_app.name.split('/')[-1]
        super(Applications, self).save(*args, **kwargs)

    # метод перегрузки для вывода объекта (изменяем отображение заголовка каждого заявления в админ панели)
    def __str__(self):
        return self.name
