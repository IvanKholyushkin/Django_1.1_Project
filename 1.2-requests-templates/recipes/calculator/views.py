from django.http import HttpResponse

from django.shortcuts import render, reverse


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
}

def home_view(request):
    pages = {
        "Омлет": reverse("omlet"),
        "Паста": reverse("pasta"),
        "Бутерброд": reverse("buter"),
    }

    context = {
        "pages": pages
    }
    return render(request, 'calculator/home.html', context)

def get_omlet(request):
    servings = int(request.GET.get('servings', 1))
    recipe = {ingredient: quantity * servings for ingredient, quantity in DATA['buter'].items()}
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

def get_pasta(request):
    servings = int(request.GET.get('servings', 1))
    recipe = {ingredient: quantity * servings for ingredient, quantity in DATA['buter'].items()}
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

def get_buter(request):
    servings = int(request.GET.get('servings', 1))
    recipe = {ingredient: quantity * servings for ingredient, quantity in DATA['buter'].items()}
    context = {
        'recipe': recipe
        }
    return render(request, 'calculator/index.html', context)


