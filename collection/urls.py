from django.urls import path

from collection import views

urlpatterns = [
    path('', views.index, name='index'),
]
