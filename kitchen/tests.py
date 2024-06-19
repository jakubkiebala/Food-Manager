import datetime

import pytest
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import Magazine, MagazineProduct, Catalog


# Create your tests here.


def test_home_view():
    url = reverse('base')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


def test_kitchen_manager_view():
    url = reverse('kitchen_manager')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


def test_magazine_start_view():
    url = reverse('magazine_start')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


def test_magazine_add_get():
    url = reverse('magazine_add')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize('name, is_cooler, status_code', [
    ('random_name', False, 302),
    ('random_name', True, 302),
    ('', False, 200)
])
def test_magazine_add_post(name, is_cooler, status_code):
    url = reverse('magazine_add')
    client = Client()
    data = {
        'name': name,
        'is_cooler': is_cooler
    }
    response = client.post(url, data)
    assert response.status_code == status_code


@pytest.mark.django_db
def test_magazine_edit_list_get(magazines):
    url = reverse('magazine_edit_list')
    client = Client()
    response = client.get(url)
    context = magazines
    response.context = context
    assert response.status_code == 200


@pytest.mark.django_db
def test_magazine_edit_get(magazines):
    magazine = magazines[3]
    url = reverse('magazine_edit',  args=(magazine.pk, ))
    client = Client()
    response = client.get(url)
    context = magazine
    response.context = magazine
    assert response.status_code == 200


@pytest.mark.django_db
def test_magazine_edit_post(magazines):
    magazine = Magazine.objects.create(name='name', is_cooler=False)
    url = reverse('magazine_edit', args=(magazine.pk,))
    client = Client()
    data = {
        'name': 'newname',
        'is_cooler': True
    }
    response = client.post(url, data)
    assert response.status_code == 302


def test_magazine_delete_list_view(magazines):
    url = reverse('magazine_delete_list')
    client = Client()
    response = client.get(url)
    context = magazines
    response.context = magazines
    assert response.status_code == 200


@pytest.mark.django_db
def test_magazine_delete_form_get(magazines):
    magazine = magazines[2]
    url = reverse('magazine_delete', args=(magazine.id,))
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_magazine_delete_form_post(magazines):
    magazine = magazines[2]
    url = reverse('magazine_delete', args=(magazine.id,))
    client = Client()
    response = client.post(url)
    assert response.status_code == 302


def test_catalog_start_view():
    url = reverse('catalog_start')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


def test_catalog_add_get():
    url = reverse('catalog_add')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize('name, status_code', [
    ('catalog', 302),
    ('', 200)
])
def test_catalog_add_post(name, status_code):
    url = reverse('catalog_add')
    client = Client()
    data = {
        'name': name
    }
    response = client.post(url, data)
    assert response.status_code == status_code


@pytest.mark.django_db
def test_catalog_edit_list_view(catalogs):
    url = reverse('catalog_edit_list')
    client = Client()
    response = client.get(url)
    context = catalogs
    response.context = context
    assert response.status_code == 200


@pytest.mark.django_db
def test_catalog_edit_get(catalogs):
    catalog = catalogs[2]
    url = reverse('catalog_edit', args=(catalog.id,))
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize('name, newname , status_code', [
    ('name', 'newname', 302),
    ('name', '', 200)
])
def test_catalog_edit_get(name, newname, status_code):
    catalog = Catalog.objects.create(name=name)
    url = reverse('catalog_edit', args=(catalog.id,))
    client = Client()
    data = {
        'name': newname
    }
    response = client.post(url, data)
    assert response.status_code == status_code


@pytest.mark.django_db
def test_catalog_delete_list_view(catalogs):
    url = reverse('catalog_delete_list')
    client = Client()
    response = client.get(url)
    context = catalogs
    response.context = context
    assert response.status_code == 200


@pytest.mark.django_db
def test_catalog_delete_get(catalogs):
    catalog = catalogs[3]
    url = reverse('catalog_delete', args=(catalog.pk,))
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_catalog_delete_post(catalogs):
    catalog = catalogs[3]
    url = reverse('catalog_delete', args=(catalog.pk,))
    client = Client()
    response = client.post(url)
    assert response.status_code == 302


def test_catalog_product_create_get():
    url = reverse('catalog_product_create')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize('name, status_code', [
    ('product', 302),
    ('', 200)
])
def test_catalog_product_create_post(name, status_code):
    url = reverse('catalog_product_create')
    client = Client()
    data = {
        'name': name
    }
    response = client.post(url, data)
    assert response.status_code == status_code


@pytest.mark.django_db
def test_products_view(magazines):
    url = reverse('products')
    client = Client()
    context = magazines
    response = client.get(url)
    response.context = context
    assert response.status_code == 200


@pytest.mark.django_db
def test_magazine_list_view(magazines):
    url = reverse('magazine_list')
    client = Client()
    response = client.get(url)
    response.context = magazines
    assert response.status_code == 200


@pytest.mark.django_db
def test_magazine_food_list_view(magazines):
    magazine = magazines[4]
    url = reverse('magazine_food_list', args=(magazine.pk, ))
    client = Client()
    context = magazine
    response = client.get(url)
    response.context = context
    assert response.status_code == 200


@pytest.mark.django_db
def test_magazine_food_list_context(magazines):
    magazine = magazines[3]
    url = reverse('magazine_food_list', args=(magazine.pk,))
    client = Client()
    context = magazine
    response = client.get(url)
    response.context = context
    assert response.context == context


@pytest.mark.django_db
@pytest.mark.parametrize('name, exp_date, status_code', [
    ('product', '2026-02-02', 302),
    ('', '2026-02-02', 200),
])
def test_magazine_product_add_post(name, exp_date, status_code, magazines):
    magazine = magazines[2]
    url = reverse('magazine_product_add', args=(magazine.id,))
    client = Client()
    received_date = datetime.date.today()
    data = {
        'name': name,
        'expiration_date': exp_date,
        'received_date': received_date,
    }
    response = client.post(url, data)
    assert response.status_code == status_code
    received_date = datetime.date.today() + datetime.timedelta(days=1)
    data = {
        'name': name,
        'expiration_date': exp_date,
        'received_date': received_date,
    }
    response = client.post(url, data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_magazine_product_delete_get(magazine_products):
    product = magazine_products[2]
    url = reverse('magazine_product_delete', args=(product.id,))
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_magazine_product_delete_post(magazines):
    product = MagazineProduct.objects.create(name='name',
                                             expiration_date=datetime.date.today(),
                                             received_date=datetime.date.today(),
                                             magazine=magazines[1])
    product_id = product.id
    url = reverse('magazine_product_delete', args=(product.id,))
    client = Client()
    response = client.post(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_catalog_list_view(catalogs):
    url = reverse('catalog_list')
    client = Client()
    response = client.get(url)
    response.context = catalogs
    assert response.status_code == 200


@pytest.mark.django_db
def test_catalog_food_list_view(catalogs):
    catalog = catalogs[3]
    url = reverse('catalog_food_list', args=(catalog.id,))
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_catalog_product_add_get(catalogs, catalog_products):
    catalog = catalogs[2]
    url = reverse('catalog_product_add', args=(catalog.id,))
    client = Client()
    response = client.get(url)
    context = {
        'catalogs': catalogs,
        'products': catalog_products
    }
    response.context = context
    assert response.status_code == 200


def test_recipies_view():
    url = reverse('recipies')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


def test_calendar_view():
    url = reverse('calendar')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
