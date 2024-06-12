import pytest
from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.


def test_home_view():
    url = reverse('base')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
