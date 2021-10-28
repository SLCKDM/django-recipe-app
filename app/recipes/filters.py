
#! maybe you shouold delete this

import django_filters

from .models import CookRecipe

class RecipeFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(RecipeFilter, self).__init__(*args, **kwargs)
        self.fields['toppings'].label = "toppings"
    class Meta:
        model = CookRecipe
        fields = {
                'title': ['exact', 'icontains'],
                'content': ['exact', 'icontains'],
                'toppings': ['exact', 'icontains'],
                }
