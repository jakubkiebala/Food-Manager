import datetime

import pytest

from kitchen.models import Magazine, MagazineProduct, Catalog, CatalogProduct


@pytest.fixture
def magazines(db):
    lst = []
    for i in range(5):
        magazine1 = Magazine.objects.create(name=f'magazine{i}', is_cooler=False)
        magazine2 = Magazine.objects.create(name=f'{i}magazine', is_cooler=True)
        lst.append(magazine1)
        lst.append(magazine2)
    return lst

@pytest.fixture
def magazine_products(magazines):
    lst = []
    magazine = magazines[1]
    exp_date = datetime.date.today() + datetime.timedelta(days=20)
    rc_date = datetime.date.today()
    for i in range(5):
        product = MagazineProduct.objects.create(name=f'product{i}', expiration_date=exp_date
                                                 , received_date=rc_date, magazine=magazine)
        lst.append(product)
    return lst


@pytest.fixture
def catalogs(db):
    lst = []
    for i in range(5):
        catalog = Catalog.objects.create(name=f'name{i}')
        lst.append(catalog)
    return lst


@pytest.fixture
def catalog_products():
    lst = []
    for i in range(5):
        product = CatalogProduct.objects.create(name=f'product{i}')
        lst.append(product)
    return lst



