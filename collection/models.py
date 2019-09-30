import requests
from bs4 import BeautifulSoup
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    amount = models.CharField(max_length=30)

    def __str__(self):
        return self.amount + ' ' + self.unit + '(s) of ' + self.name


class IngredientManager(models.Manager):
    def create_ingredient(self, name, unit, amount):
        ingredient = self.create(name=name, unit=unit, amount=amount)
        return ingredient

#
# class IngredientAmount(models.Model):
#     amount = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
#     recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
#     ingredient = models.ForeignKey(
#         'Ingredient', on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return 'Amount of ' + self.ingredient.name
#
#
# class IngredientAmountManager(models.Manager):
#     def create_ingredient_amount(self, amount, recipe, ingredient, name, unit):
#         if ingredient is None:
#             ingredient = IngredientManager.create_ingredient(name, unit)
#         else:
#             ingredient = ingredient
#         ingredient_amount = IngredientAmount.create()
#


class RecipeManager(models.Manager):
    def parse_link(self, link):
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'html.parser')

        ingredient_group = soup.find(class_='wprm-recipe-ingredients')
        ingredients = []
        if ingredient_group:
            ingredient_soup = ingredient_group.find_all('li')
            for ingredient in ingredient_soup:
                ingredients.append(ingredient.text)

        title = soup.find(class_='entry-title').text
        author = soup.find(class_='wprm-recipe-author').text
        time = soup.find(class_='wprm-recipe-total_time').text
        time += ' ' + soup.find(class_='wprm-recipe-total_time').find_next_sibling().text
        servings = soup.find(class_='wprm-recipe-servings').text
        instructions = soup.find(class_='wprm-recipe-instructions-container').text
        img_src = soup.find(class_='wprm-recipe-image').find('img')['src']
        Recipe.objects.create(
            title=title,
            author=author,
            ingredient_strings=ingredients,
            time=time,
            servings=servings,
            instructions=instructions,
            link=link,
            img_src=img_src,
            notes='none',
        )


class Recipe(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100, null=True, blank=True)
    ingredient_objects = models.ManyToManyField(Ingredient, blank=True)
    ingredient_strings = ArrayField(models.CharField(max_length=250), null=True, blank=True)
    time = models.CharField(max_length=20, null=True, blank=True)
    servings = models.IntegerField(null=True, blank=True)
    instructions = models.TextField()
    link = models.CharField(max_length=250)
    img_src = models.CharField(max_length=250, null=True)
    notes = models.TextField(null=True, blank=True)

    objects = RecipeManager()

    def __str__(self):
        return self.title

