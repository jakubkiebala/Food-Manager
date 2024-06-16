import pytest

from kitchen.models import Magazine


@pytest.fixture
def magazines(db):
    lst = []
    for i in range(5):
        magazine1 = Magazine.objects.create(name=f'magazine{i}', is_cooler=False)
        magazine2 = Magazine.objects.create(name=f'{i}magazine', is_cooler=True)
        lst.append(magazine1)
        lst.append(magazine2)
    return lst
