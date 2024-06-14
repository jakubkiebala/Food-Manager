from django.shortcuts import render
from django.views import View


# Create your views here.


class KitchenManagerView(View):
    def get(self, request):
        return render(request, 'kitchen/kitchen_manager_start.html')


class CatalogStartView(View):
    def get(self, request):
        return render(request, 'kitchen/kitchen_manager_catalog_start.html')


class ProductsView(View):
    def get(self, request):
        food_containers = ('Górna Szafka Po Lewej', 'Lodówka', 'Dolna Szafka Po Prawej')
        return render(request, 'kitchen/products_start.html', {'food_containers': food_containers})


class RecipiesView(View):
    def get(self, request):
        return render(request, 'kitchen/recipies_start.html')


class CalendarView(View):
    def get(self, request):
        return render(request, 'kitchen/calendar_start.html')
