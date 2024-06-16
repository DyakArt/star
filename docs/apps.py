from django.apps import AppConfig


class DocsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'docs'
    # меняем название группы в админ панели
    verbose_name = 'Документы и заявления'
