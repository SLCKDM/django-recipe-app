from django.contrib import admin
from .models import CookRecipe, Topping


class ToppingAdmin(admin.ModelAdmin):
    """ cutomizing Topping model in admin panel """
    list_filter = ('name',)
    search_fields = ('name',)


@admin.display(description='Ингредиенты')
def get_toppings(obj):
    """ function that returns toppings user in recipe """
    return tuple(obj.toppings.all())


class CookRecipeAdmin(admin.ModelAdmin):
    """ cutomizing CookRecipe model in admin panel """
    list_display = ('title', get_toppings)
    search_fields = ('title',)


# register models and cutomization in admin panel
admin.site.register(CookRecipe, CookRecipeAdmin)
admin.site.register(Topping, ToppingAdmin)
