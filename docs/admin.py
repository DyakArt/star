from django.contrib import admin

# чтобы таблицы отображались в админ панели, нужно зарегистрировать их здесь

# импортируем таблицы из models
from .models import Documents, Applications

# регистрируем таблицу Documents в админ панели
admin.site.register(Documents)

# регистрируем таблицу Applications в админ панели
admin.site.register(Applications)
