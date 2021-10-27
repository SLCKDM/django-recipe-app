from django.contrib import admin
from .models import CookRecipe, Topping
from django.utils.html import mark_safe
import itertools

class ToppingAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name',)
    

@admin.display(description='Name')
def get_toppings(obj):
    return tuple(obj.toppings.all())
class CookRecipeAdmin(admin.ModelAdmin):

    list_display = ('title', get_toppings)
    search_fields = ('title',)


admin.site.register(CookRecipe, CookRecipeAdmin)
admin.site.register(Topping, ToppingAdmin)
