# Generated by Django 5.0.6 on 2024-06-16 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_reserve'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1300, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Полезная информация',
                'verbose_name_plural': 'Полезная информация',
                'db_table': 'info',
            },
        ),
    ]