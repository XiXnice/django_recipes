from django.core.paginator import Paginator
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def omlet(request):
    ing_number = int(request.GET.get('servings', 1))
    q = DATA['omlet']
    for z, x in q.items():
        q[z] = round(x * ing_number, 1)
    context = {
        'recipe': q,
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    ing_number = int(request.GET.get('servings', 1))
    q = DATA['pasta']
    for z, x in q.items():
        q[z] = round(x * ing_number, 1)
    context = {
        'recipe': q,
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    ing_number = int(request.GET.get('servings', 1))
    q = DATA['buter']
    for z, x in q.items():
        q[z] = round(x * ing_number, 1)
    context = {
        'recipe': q,
    }
    return render(request, 'calculator/index.html', context)
