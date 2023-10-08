from django.shortcuts import render, get_object_or_404

from .models import MenuModel


def menu(request, named_url):
    tree = MenuModel.objects.filter(named_url=named_url).get_descendants(include_self=True)
    return render(request, 'menu.html', {'tree': tree})