import pytest
from django.test import TestCase, Client
from django.urls import reverse

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


def test_products_view():
    url = reverse('products')
    client = Client()
    response = client.get(url)
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
