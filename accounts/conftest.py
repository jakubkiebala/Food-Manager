import pytest
from django.contrib.auth.models import User


@pytest.fixture
def users(db):
    lst = []
    for i in range(0, 10):
        lst.append(User.objects.create_user(username=f'username{i}', password='password'))
    return lst
