import pytest
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.


def test_register_user_get():
    url = reverse('register_user')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize('username, password1, password2, result', [
    ('random_username', '123456', '123456', 302),
    ('random_username', '123456', '654321', 200),
    ('random_username', '654321', '123456', 200),
])
def test_register_user_post(username, password1, password2, result):
    url = reverse('register_user')
    client = Client()
    data = {
        'username': username,
        'password1': password1,
        'password2': password2
    }
    response = client.post(url, data)
    assert response.status_code == result
    user = User.objects.filter(username=username).exists()
    if result == 302:
        assert user
    else:
        assert not user


def test_login_user_get():
    url = reverse('login_user')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize('username, password, status_code', [
    ('username1', 'password', 302),
    ('username1', 'incorrect_password', 200),
    ('incorrect_username', 'any_password', 200),
])
def test_login_user_post(username, password, status_code, users):
    url = reverse('login_user')
    client = Client()
    data = {
        'username': username,
        'password': password
    }
    response = client.post(url, data)
    assert response.status_code == status_code
    if status_code == 302:
        assert response.wsgi_request.user.is_authenticated
    else:
        assert not response.wsgi_request.user.is_authenticated


def test_logout_view():
    url = reverse('logout')
    client = Client()
    response = client.get(url)
    assert response.status_code == 302


def test_logout_view2():
    url = reverse('logout')
    client = Client()
    response = client.get(url)
    redirected_url = reverse('base')
    assert response.url == redirected_url
