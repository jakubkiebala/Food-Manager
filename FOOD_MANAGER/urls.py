"""
URL configuration for FOOD_MANAGER project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from kitchen import views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base/base.html'), name='base'),
    path('kitchen_manager/', views.KitchenManagerView.as_view(), name='kitchen_manager'),
    path('kitchen_manager/magazine/start/', views.MagazineStartView.as_view(), name='magazine_start'),
    path('kitchen_manager/magazine/add', views.MagazineAddView.as_view(), name='magazine_add'),
    path('kitchen_manager/magazine/edit/', views.MagazineEditListView.as_view(), name='magazine_edit_list'),
    path('kitchen_manager/magazine/edit/<int:pk>/', views.MagazineEditView.as_view(), name='magazine_edit'),
    path('kitchen_manager/magazine/delete/', views.MagazineDeleteListView.as_view(), name='magazine_delete_list'),
    path('kitchen_manager/magazine/delete/<int:pk>/', views.MagazineDeleteView.as_view(), name='magazine_delete'),
    path('kitchen_manager/catalog/start/', views.CatalogStartView.as_view(), name='catalog_start'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('products/magazine/<int:pk>/food_list/', views.MagazineFoodListView.as_view(), name='magazine_food_list'),
    path('recipies/', views.RecipiesView.as_view(), name='recipies'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('register/', account_views.RegisterUserView.as_view(), name='register_user'),
    path('login/', account_views.LoginUserView.as_view(), name='login_user'),
    path('logout/', account_views.LogoutView.as_view(), name='logout'),
]
