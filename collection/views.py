from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from collection.models import Recipe


@login_required
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'collection/base.html', {'recipes': recipes})
