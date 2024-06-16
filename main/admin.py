from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# чтобы таблицы отображались в админ панели, нужно зарегистрировать их здесь

# импортируем таблицы из models
from .models import News, HistoryCompany, Reserve, Info, Policy, UserProfile

# регистрируем таблицу News в админ панели
admin.site.register(News)


class CheckCountRecordsInTables(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Проверяем, существует ли уже запись в таблице
        if self.model.objects.count() > 0:
            return False
        else:
            # Если записей ещё нет, разрешаем добавление
            return True


# наследуем класс CheckCountRecordsInTables для проверки количества записей
class HistoryCompanyAdmin(CheckCountRecordsInTables):
    pass


class ReserveAdmin(CheckCountRecordsInTables):
    pass


class InfoAdmin(CheckCountRecordsInTables):
    pass


class PolicyAdmin(CheckCountRecordsInTables):
    pass


class UserInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmins(UserAdmin):
    inlines = (UserInLine,)


# регистрируем таблицу HistoryCompany, HistoryCompanyAdmin в админ панели
admin.site.register(HistoryCompany, HistoryCompanyAdmin)

# регистрируем таблицу Reserve, ReserveAdmin в админ панели
admin.site.register(Reserve, ReserveAdmin)

# регистрируем таблицу Reserve, ReserveAdmin в админ панели
admin.site.register(Info, InfoAdmin)

# регистрируем таблицу Policy, PolicyAdmin в админ панели
admin.site.register(Policy, PolicyAdmin)

admin.site.unregister(User)
# Регистрация модели User, UserAdmins в админ-панели
admin.site.register(User, UserAdmins)
