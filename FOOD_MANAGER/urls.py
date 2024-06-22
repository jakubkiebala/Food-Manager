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
    path('kitchen_manager/catalog/add/', views.CatalogAddView.as_view(), name='catalog_add'),
    path('kitchen_manager/catalog/edit/', views.CatalogEditListView.as_view(), name='catalog_edit_list'),
    path('kitchen_manager/catalog/edit/<int:pk>/', views.CatalogEditView.as_view(), name='catalog_edit'),
    path('kitchen_manager/catalog/delete/', views.CatalogDeleteListView.as_view(), name='catalog_delete_list'),
    path('kitchen_manager/catalog/delete/<int:pk>', views.CatalogDeleteView.as_view(), name='catalog_delete'),
    path('kitchen_manager/catalog/product/create', views.CatalogProductCreate.as_view(), name='catalog_product_create'),
    path('products/start/', views.ProductsView.as_view(), name='products'),
    path('products/magazine/list/', views.MagazineListView.as_view(), name='magazine_list'),
    path('products/magazine/<int:pk>/food_list/', views.MagazineFoodListView.as_view(), name='magazine_food_list'),
    path('products/magazine/<int:pk>/product/add/', views.MagazineProductAddView.as_view(),
         name='magazine_product_add'),
    path('products/magazine_product/<int:pk>/delete/', views.MagazineProductDelete.as_view(),
         name='magazine_product_delete'),
    path('products/magazine_object/<int:pk>/edit/', views.MagazineProductEdit.as_view(), name='magazine_product_edit'),
    path('products/catalog/list/', views.CatalogListView.as_view(), name='catalog_list'),
    path('products/catalog/<int:pk>/food_list/', views.CatalogFoodListView.as_view(), name='catalog_food_list'),
    path('products/catalog/<int:pk>/product/add/', views.CatalogProductAddView.as_view(), name='catalog_product_add'),
    path('recipies/', views.RecipiesView.as_view(), name='recipies'),
    path('shopping_list/', views.ShoppingListView.as_view(), name='shopping_list'),
    path('register/', account_views.RegisterUserView.as_view(), name='register_user'),
    path('login/', account_views.LoginUserView.as_view(), name='login_user'),
    path('logout/', account_views.LogoutView.as_view(), name='logout'),
]
