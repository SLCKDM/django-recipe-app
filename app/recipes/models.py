from django.db import models


class Topping(models.Model):
    """ Topping model

    :name: is a textform, that takes unique igridient name
    """
    name = models.CharField(
        max_length=50,
        verbose_name='Ингредиент',
        unique=True
    )

    class Meta:
        """ Topping  Meta class

        :ordering: order of entries
        :verbose_name: name in the panel
        :verbose_name_plural: name in the panel in plural
        """
        ordering = ['name']
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        """ object representation """
        return self.name.lower()


class CookRecipe(models.Model):
    """ CookRecipe model

    :title: is a textform, that takes recipe title
    :content: recipe description
    :toppings: many to many field, takes chosen 
    toppings from Topping model
    """
    title = models.CharField(max_length=50, verbose_name='Рецепт')
    content = models.TextField(max_length=512, verbose_name='Описание')
    toppings = models.ManyToManyField(
        "Topping",
        verbose_name='Ингредиенты',
        related_name='recipe_toppings'
    )

    class Meta:
        """ CookRecipe Meta class

        :ordering: order of entries
        :verbose_name: name in the panel
        :verbose_name_plural: name in the panel in plural
        """
        ordering = ['title']
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        """ object representation """
        return self.title
