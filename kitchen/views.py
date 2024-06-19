from datetime import datetime

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView

from kitchen.forms import MagazineAddForm
from kitchen.models import Magazine, MagazineProduct, Catalog, CatalogProduct


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
        user = request.user if request.user.is_authenticated else None
        if name:
            Magazine.objects.create(name=name, is_cooler=is_cooler, user=user)
            return redirect('magazine_start')
        else:
            return render(request, 'kitchen_manager/magazine_add_form.html', {'error': 'Podaj Nazwę'})


class MagazineEditListView(View):
    def get(self, request):
        user = request.user if request.user.is_authenticated else None
        food_containers = Magazine.objects.filter(user=user)
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
            return redirect('magazine_start')
        else:
            return render(request, 'kitchen_manager/magazine_edit_form.html', {'error': 'Podaj Nazwę'})


class MagazineDeleteListView(View):
    def get(self, request):
        user = request.user if request.user.is_authenticated else None
        food_containers = Magazine.objects.filter(user=user)
        return render(request, 'kitchen_manager/magazine_delete_list.html', {'food_containers': food_containers})


class MagazineDeleteView(View):
    def get(self, request, pk):
        magazine = Magazine.objects.get(id=pk)
        return render(request, 'kitchen_manager/magazine_delete_form.html', {'magazine': magazine})

    def post(self, request, pk):
        magazine = Magazine.objects.get(id=pk)
        magazine.delete()
        return redirect('magazine_start')


class CatalogStartView(View):
    def get(self, request):
        return render(request, 'kitchen_manager/catalog_start.html')


class CatalogAddView(View):
    def get(self, request):
        return render(request, 'kitchen_manager/catalog_add_form.html')

    def post(self, request):
        name = request.POST.get('name')
        user = request.user if request.user.is_authenticated else None
        if name:
            Catalog.objects.create(name=name, user=user)
            return redirect('catalog_start')
        else:
            return render(request, 'kitchen_manager/catalog_add_form.html', {'error': 'Podaj Nazwę'})


class CatalogEditListView(View):
    def get(self, request):
        user = request.user if request.user.is_authenticated else None
        catalogs = Catalog.objects.filter(user=user)
        return render(request, 'kitchen_manager/catalog_edit_list.html', {'catalogs': catalogs})


class CatalogEditView(View):
    def get(self, request, pk):
        catalog = Catalog.objects.get(id=pk)
        return render(request, 'kitchen_manager/catalog_edit_form.html', {'catalog': catalog})

    def post(self, request, pk):
        catalog = Catalog.objects.get(id=pk)
        name = request.POST.get('name')
        if name:
            catalog.name = name
            catalog.save()
            return redirect('catalog_start')
        else:
            return render(request, 'kitchen_manager/catalog_edit_form.html', {'error': 'Podaj Nazwę'})


class CatalogDeleteListView(View):
    def get(self, request):
        user = request.user if request.user.is_authenticated else None
        catalogs = Catalog.objects.filter(user=user)
        return render(request, 'kitchen_manager/catalog_delete_list.html', {'catalogs': catalogs})


class CatalogDeleteView(View):
    def get(self, request, pk):
        catalog = Catalog.objects.get(id=pk)
        return render(request, 'kitchen_manager/catalog_delete_form.html', {'catalog': catalog})

    def post(self, request, pk):
        catalog = Catalog.objects.get(id=pk)
        catalog.delete()
        return redirect('catalog_start')


class CatalogProductCreate(View):
    def get(self, request):
        return render(request, 'kitchen_manager/catalog_product_create.html')

    def post(self, request):
        user = request.user if request.user.is_authenticated else None
        name = request.POST.get('name')
        if name:
            CatalogProduct.objects.create(name=name, user=user)
            return redirect('catalog_start')
        else:
            return render(request, 'kitchen_manager/catalog_product_create.html', {'error': 'Podaj Nazwę'})
#
# Products Branches
#


class ProductsView(View):
    def get(self, request):
        return render(request, 'products/products_start.html')


class MagazineListView(View):
    def get(self, request):
        user = request.user if request.user.is_authenticated else None
        food_containers = Magazine.objects.filter(user=user)
        return render(request, 'products/magazine_list.html', {'food_containers': food_containers})


class MagazineFoodListView(View):
    def get(self, request, pk):
        magazine = Magazine.objects.get(id=pk)
        products = MagazineProduct.objects.filter(magazine=magazine)
        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'products/magazine_product_list.html',
                      {'magazine': magazine, 'products': products, 'page_obj': page_obj})


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
            return redirect('magazine_food_list', magazine.id)
        return render(request, 'products/magazine_product_add.html', {'magazine': magazine})


class MagazineProductDelete(View):
    def get(self, request, pk):
        product = MagazineProduct.objects.get(id=pk)
        return render(request, 'products/magazine_product_delete_form.html', {'product': product})

    def post(self, request, pk):
        product = MagazineProduct.objects.get(id=pk)
        product.delete()
        return redirect('magazine_food_list', product.magazine.id)


class MagazineProductEdit(View):
    def get(self, request, pk):
        product = MagazineProduct.objects.get(id=pk)
        return render(request, 'products/magazine_product_edit.html', {'product': product})

    def post(self, request, pk):
        product = MagazineProduct.objects.get(id=pk)
        is_opened = request.POST.get('is_opened')
        name = request.POST.get('name')
        expiration_date = request.POST.get('expiration_date')
        received_date = request.POST.get('received_date')
        expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()
        received_date = datetime.strptime(received_date, '%Y-%m-%d').date()
        if name != '' and received_date <= datetime.today().date():
            if is_opened == 'tak':
                product.name = name
                product.expiration_date = expiration_date
                product.is_opened = True
                product.received_date = received_date
                product.save()
                return redirect('magazine_food_list', product.magazine.id)
            else:
                product.name = name
                product.expiration_date = expiration_date
                product.is_opened = False
                product.received_date = received_date
                product.save()
                return redirect('magazine_food_list', product.magazine.id)
        return render(request, 'products/magazine_product_edit.html', {'product': product})


class CatalogListView(View):
    def get(self, request):
        user = request.user if request.user.is_authenticated else None
        catalogs = Catalog.objects.filter(user=user)
        return render(request, 'products/catalog_list.html', {'catalogs': catalogs})


class CatalogFoodListView(View):
    def get(self, request, pk):
        catalog = Catalog.objects.get(id=pk)
        products = CatalogProduct.objects.filter(catalog=catalog)
        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'products/catalog_product_list.html',
                      {'catalog': catalog, 'products': products, 'page_obj': page_obj})


class CatalogProductAddView(View):
    def get(self, request, pk):
        user = request.user if request.user.is_authenticated else None
        products = CatalogProduct.objects.filter(user=user)
        catalog = Catalog.objects.get(id=pk)
        return render(request, 'products/catalog_product_add.html', {'products': products,
                                                                     'catalog': catalog})

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
