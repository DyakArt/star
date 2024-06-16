from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    # меняем название группы в админ панели
    verbose_name = 'Главная и остальные страницы'
