# Generated by Django 3.2.8 on 2021-10-27 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Ингридиент')),
            ],
            options={
                'ordering': ['name', '-name'],
            },
        ),
        migrations.CreateModel(
            name='CookRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Рецепт')),
                ('content', models.TextField(max_length=512, verbose_name='Описание')),
                ('toppings', models.ManyToManyField(related_name='recipe_toppings', to='recipes.Topping', verbose_name='Ингридиенты')),
            ],
            options={
                'ordering': ['title', '-title'],
            },
        ),
    ]
