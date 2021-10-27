from django.db import models

class Topping(models.Model):
    """ Ингридиент """
    name = models.CharField(max_length=50, verbose_name='Ингридиент', unique=True)
    
    class Meta:
        ordering = ['name']
        verbose_name="Ингридиент"
        verbose_name_plural="Ингридиенты"
    
    def __str__(self):
        return self.name.lower()
    
class CookRecipe(models.Model):
    """ Рецепт """
    title = models.CharField(max_length=50, verbose_name='Рецепт')
    content = models.TextField(max_length=512, verbose_name='Описание')
    toppings = models.ManyToManyField("Topping", verbose_name='Ингридиенты', related_name='recipe_toppings')

    class Meta:
        ordering = ['title']
        verbose_name="Рецепт"
        verbose_name_plural="Рецепты"
        
    def __str__(self):
        return self.title
