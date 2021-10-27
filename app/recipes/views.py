from django.shortcuts import render
from .models import CookRecipe, Topping


def index(request):
    recipes = CookRecipe.objects.all()
    context = {
        'recipes':recipes,
    }
    return render(request, 'recipes/index.html', context=context)

# Create your views here.
