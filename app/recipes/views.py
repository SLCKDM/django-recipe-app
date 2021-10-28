from django.db.models.query import EmptyQuerySet
from django.shortcuts import render

from .models import CookRecipe, Topping


def index(request):
    default = CookRecipe.objects.all()
    q = request.GET.get('search')
    if q:
        q1 = CookRecipe.objects.filter(title__icontains=q)
        try:
            q2 = CookRecipe.objects.filter(toppings__in=[Topping.objects.get(name__icontains=q).id])
        except:
            q2 = CookRecipe.objects.none()
        recipes = q1.union(q2)
    else:
        recipes = default
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/index.html', context=context)
