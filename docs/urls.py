from django.urls import path

from docs import views

# необходимо указать имя приложения для пространства имён (namespace), чтобы не было ошибки
app_name = 'docs'

# первый аргумент в path - это адрес конкретной страницы,
# второй аргумент - регистрация представления, которое будет закреплено за этим адресом
# третий аргумент - для тегов в html-документах, чтобы можно было обращаться к этим ссылкам по имени
urlpatterns = [
    # путь для страницы с документами
    path('', views.documents, name='documents'),
    # путь для страницы с заявлениями
    path('applications/', views.applications, name='applications'),
]
