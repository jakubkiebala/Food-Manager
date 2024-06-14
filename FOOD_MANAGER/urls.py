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
    path('products/', views.ProductsView.as_view(), name='products'),
    path('recipies/', views.RecipiesView.as_view(), name='recipies'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('register/', account_views.RegisterUserView.as_view(), name='register_user'),
    path('login/', account_views.LoginUserView.as_view(), name='login_user'),
    path('logout/', account_views.LogoutView.as_view(), name='logout'),
    path('kitchen_manager/catalog/start/', views.CatalogStartView.as_view(), name='catalog_start')
]
