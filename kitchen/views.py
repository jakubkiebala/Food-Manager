from django.shortcuts import render, redirect
from django.views import View

from kitchen.forms import MagazineAddForm
from kitchen.models import Magazine


# Create your views here.

#
# Kitchen Manager Branches
#


class KitchenManagerView(View):
    def get(self, request):
        return render(request, 'kitchen/kitchen_manager_start.html')


class MagazineStartView(View):
    def get(self, request):
        return render(request, 'kitchen/k_m_magazine_start.html')


class MagazineAddView(View):
    def get(self, request):
        form = MagazineAddForm()
        first_title = 'Zarządzaj Kuchnią'
        second_title = 'Dodaj Magazyn'
        return render(request, 'base/adding_form.html', {
            'first_title': first_title,
            'second_title': second_title,
            'form': form
        })

    def post(self, request):
        form = MagazineAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            is_cooler = form.cleaned_data['is_cooler']
            Magazine.objects.create(name=name)
            return redirect('products')
        first_title = 'Zarządzaj Kuchnią'
        second_title = 'Dodaj Magazyn'
        return render(request, 'base/adding_form.html', {
            'first_title': first_title,
            'second_title': second_title,
            'form': form
        })


class CatalogStartView(View):
    def get(self, request):
        return render(request, 'kitchen/k_m_catalog_start.html')

#
# Products Branches
#


class ProductsView(View):
    def get(self, request):
        food_containers = Magazine.objects.all()
        return render(request, 'kitchen/products_start.html', {'food_containers': food_containers})

#
# Recipies Branches
#


class RecipiesView(View):
    def get(self, request):
        return render(request, 'kitchen/recipies_start.html')

#
# Calendar Branches
#


class CalendarView(View):
    def get(self, request):
        return render(request, 'kitchen/calendar_start.html')
