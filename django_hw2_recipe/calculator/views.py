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
    template_name = 'calculator/home.html'
    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def recipe(request, name, title):
    template_name = 'calculator/index.html'
    person_count = int(request.GET.get('servings', 1))
    if str(person_count)[-1] == '1':
        final_symbol = 'а'
    else:
        final_symbol = ''
    recipe_dict = {}
    for key, value in DATA[name].items():
        recipe_dict[key] = round(value * person_count, 2)
    context = {
        'title': title,
        'recipe': recipe_dict,
        'person_count': person_count,
        'final_symbol': final_symbol,
        'home': reverse('home')
    }
    return render(request, template_name, context)


def omlet(request):
    return recipe(request, 'omlet', 'омлета')


def pasta(request):
    return recipe(request, 'pasta', 'пасты')


def buter(request):
    return recipe(request, 'buter', 'бутерброда')
