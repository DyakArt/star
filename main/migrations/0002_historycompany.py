# Generated by Django 5.0.6 on 2024-06-16 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph_one', models.TextField(max_length=700, verbose_name='Первый абзац')),
                ('paragraph_two', models.TextField(max_length=500, verbose_name='Второй абзац')),
            ],
            options={
                'verbose_name': 'История компании',
                'db_table': 'history_company',
            },
        ),
    ]
