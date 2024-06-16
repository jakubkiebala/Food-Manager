from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView

from kitchen.forms import MagazineAddForm
from kitchen.models import Magazine, MagazineProduct


# Create your views here.

#
# Kitchen Manager Branches
#


class KitchenManagerView(View):
    def get(self, request):
        return render(request, 'kitchen_manager/kitchen_manager_start.html')


class MagazineStartView(View):
    def get(self, request):
        return render(request, 'kitchen_manager/magazine_start.html')


class MagazineAddView(View):
    def get(self, request):
        return render(request, 'kitchen_manager/magazine_add_form.html')

    def post(self, request):
        name = request.POST.get('name')
        is_cooler = request.POST.get('is_cooler') == 'on'
        if name:
            Magazine.objects.create(name=name, is_cooler=is_cooler)
            return redirect('products')
        else:
            return render(request, 'kitchen_manager/magazine_add_form.html', {'error': 'Podaj Nazwę'})


class MagazineEditListView(View):
    def get(self, request):
        food_containers = Magazine.objects.all()
        return render(request, 'kitchen_manager/magazine_edit_list.html', {'food_containers': food_containers})


class MagazineEditView(View):
    def get(self, request, pk):
        magazine = Magazine.objects.get(id=pk)
        return render(request, 'kitchen_manager/magazine_edit_form.html', {'magazine': magazine})

    def post(self, request, pk):
        magazine = Magazine.objects.get(id=pk)
        name = request.POST.get('name')
        is_cooler = request.POST.get('is_cooler') == 'on'
        if name:
            magazine.name = name
            magazine.is_cooler = is_cooler
            magazine.save()
            return redirect('products')
        else:
            return render(request, 'kitchen_manager/magazine_add_form.html', {'error': 'Podaj Nazwę'})


class MagazineDeleteListView(View):
    def get(self, request):
        food_containers = Magazine.objects.all()
        return render(request, 'kitchen_manager/magazine_delete_list.html', {'food_containers': food_containers})


class MagazineDeleteView(View):
    def get(self, request, pk):
        magazine = Magazine.objects.get(id=pk)
        return render(request, 'kitchen_manager/magazine_delete_form.html', {'magazine': magazine})

    def post(self, request, pk):
        magazine = Magazine.objects.get(id=pk)
        magazine.delete()
        food_containers = Magazine.objects.all()
        return render(request, 'products/products_start.html', {'food_containers': food_containers})


class CatalogStartView(View):
    def get(self, request):
        return render(request, 'kitchen_manager/catalog_start.html')


#
# Products Branches
#


class ProductsView(View):
    def get(self, request):
        food_containers = Magazine.objects.all()
        return render(request, 'products/products_start.html', {'food_containers': food_containers})


class MagazineFoodListView(View):
    def get(self, request, pk):
        magazine = Magazine.objects.get(id=pk)
        products = MagazineProduct.objects.filter(magazine=magazine)
        return render(request, 'products/magazine_product_list.html', {'magazine': magazine,
                                                                       'products': products})


class MagazineProductAddView(View):
    def get(self, request, pk):
        magazine = Magazine.objects.get(id=pk)
        return render(request, 'products/magazine_product_add.html', {'magazine': magazine})

    def post(self, request, pk):
        magazine = Magazine.objects.get(id=pk)
        name = request.POST.get('name')
        expiration_date = request.POST.get('expiration_date')
        received_date = request.POST.get('received_date')
        expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()
        received_date = datetime.strptime(received_date, '%Y-%m-%d').date()
        if name != '' and received_date <= datetime.today().date():
            MagazineProduct.objects.create(name=name, expiration_date=expiration_date, received_date=received_date,
                                           magazine=magazine)
            products = MagazineProduct.objects.filter(magazine=magazine)
            return redirect('magazine_food_list', magazine.id)
        return render(request, 'products/magazine_product_add.html', {'magazine': magazine})


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
