from django.contrib import admin, messages

# чтобы таблицы отображались в админ панели, нужно зарегистрировать их здесь

# импортируем таблицы из models
from .models import News, HistoryCompany

# регистрируем таблицу News в админ панели
admin.site.register(News)


class HistoryCompanyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Проверяем, существует ли уже запись истории компании
        existing_records_count = HistoryCompany.objects.count()
        if existing_records_count > 0:
            return False
        else:
            # Если записей ещё нет, разрешаем добавление
            return True


# регистрируем таблицу HistoryCompany в админ панели
admin.site.register(HistoryCompany, HistoryCompanyAdmin)
