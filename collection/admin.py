from django.contrib import admin
from .models import Recipe, Ingredient, IngredientAmount


class IngredientInLine(admin.StackedInline):
    model = Recipe.ingredients.through
    extra = 3


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'link', 'img_src']}),
        ('Content', {'fields': ['instructions']})
    ]
    inlines = [IngredientInLine]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
#
#
# @admin.register(IngredientAmount)
# class IngredientAmountAdmin(admin.ModelAdmin):
#     pass
