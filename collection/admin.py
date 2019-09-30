from django.contrib import admin
from .models import Recipe, Ingredient


# class IngredientInLine(admin.StackedInline):
#     model = Recipe.ingredients
#     extra = 3


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
#
#
# @admin.register(IngredientAmount)
# class IngredientAmountAdmin(admin.ModelAdmin):
#     pass
