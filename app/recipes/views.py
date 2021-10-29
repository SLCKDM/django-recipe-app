from django.shortcuts import render

from .models import CookRecipe, Topping


def recipes_response(search_query):
    """ processing the request 
    returns recipe objects that contain requested query 
    """
    q1 = CookRecipe.objects.filter(title__icontains=search_query)
    try:
        q2 = CookRecipe.objects.filter(
            toppings__in=[Topping.objects.get(name__icontains=search_query).id])
    except:
        q2 = CookRecipe.objects.none()
    return q1.union(q2)


def index(request):
    """ Root url view 

    if 'search' GET request were called returns also 'search' query result using
    the function recipes_query()
    """
    recipes = CookRecipe.objects.all()
    request_query = request.GET.get('search')
    if request_query:
        recipes = recipes_response(request_query)
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/index.html', context=context)
