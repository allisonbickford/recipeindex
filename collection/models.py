from django.db import models


class IngredientAmount(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(
        'Ingredient', on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Amount of ' + self.ingredient.name


class Ingredient(models.Model):
    EACH = 'EACH'
    CUP = 'CUP'
    TBS = 'TABLESPOON'
    TSP = 'TEASPOON'
    OZ = 'OUNCE'
    LB = 'POUND'

    UNIT_CHOICES = [
        (EACH, 'Each'),
        (CUP, 'Cup'),
        (TBS, 'Tablespoon'),
        (TSP, 'teaspoon'),
        (OZ, 'Ounce'),
        (LB, 'Pound'),
    ]
    name = models.CharField(max_length=30)
    unit = models.IntegerField(choices=UNIT_CHOICES)

    def __str__(self):
        if self.UNIT_CHOICES[self.unit][self.unit] == self.EACH:
            return self.name + '(s)'
        return (self.UNIT_CHOICES[self.unit][self.unit]) + "(s) of " + self.name


class Recipe(models.Model):
    title = models.CharField(max_length=250)
    ingredients = models.ManyToManyField(Ingredient, through=IngredientAmount)
    instructions = models.TextField()
    link = models.CharField(max_length=100)
    img_src = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title
