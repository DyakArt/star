# Generated by Django 5.0.6 on 2024-06-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_remove_vacfiles_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacfiles',
            name='file_name',
            field=models.CharField(blank=True, default='Скачать бланк', max_length=255, null=True, verbose_name='Название файла'),
        ),
    ]