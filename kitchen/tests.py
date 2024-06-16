import pytest
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import Magazine


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


def test_catalog_start_view():
    url = reverse('catalog_start')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_products_view(magazines):
    url = reverse('products')
    client = Client()
    context = magazines
    response = client.get(url)
    response.context = context
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
def test_magazine_food_list_view(magazines):
    magazine = magazines[4]
    url = reverse('magazine_product_add', args=(magazine.pk, ))
    client = Client()
    context = magazine
    response = client.get(url)
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
