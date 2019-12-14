import os
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from collection.models import Recipe
from bs4 import BeautifulSoup


@login_required
def index(request):
    recipes = Recipe.objects.all()
    if request.method == 'POST':
        value = request.POST.get('recipe-link')

        # COLLECT TRAINING DATA
        # r = requests.get(value)
        # soup = BeautifulSoup(r.text, 'html.parser')
        # project_root = os.path.dirname(os.path.dirname(__file__))
        # file_name = str(len(os.listdir(os.path.join(project_root, 'data/train')))) + '.txt'
        # file = open(os.path.join(project_root, 'data/train', file_name), "w")
        # file.write(soup.get_text())
        # print("wrote to file: ", file_name)

        # ADD TO INDEX
        Recipe.objects.parse_link(value)

    return render(request, 'collection/base.html', {'recipes': recipes})


@login_required
def delete(request, pk):
    Recipe.objects.get(pk=pk).delete()
    return redirect('index')

