from .models import Documents, Applications
from django.db.models import Q
from . import models


# функция для поиска
def q_search(query, docs=None, apps=None):

    if docs:
        obj = getattr(models, "Documents")
        name = "name_document__iregex"
    else:
        obj = getattr(models, "Applications")
        name = "name__iregex"
    # по идентификатору
    # if query.isdigit() and len(query) <= 5:
    #     return obj.objects.filter(id=int(query))

    # по словам
    # создаем токены запроса (каждое отдельное слово, которое имеет смысл в поиске)
    keywords = [word for word in query.split()]
    q_objects = Q()

    # |= - как +=, добавляется "или"
    for token in keywords:
        # по каждому слову, которое введёт пользователь, нужно провести поиск и прикинуть, что можем предложить
        q_objects |= Q(**{name: token})

    return obj.objects.filter(q_objects)
