import pytest
from pytest_django.asserts import assertQuerysetEqual

from catalogue.models import Vendor, Product
from catalogue.tests.factories import VendorFactory, ProductFactory


pytestmark = pytest.mark.django_db


class TestVendorModel:
    def test__str_(self, vendor):
        assert vendor.__str__() == vendor.name
        assert str(vendor) == vendor.name

    def test_get_absolute_url(self, vendor):
        url = vendor.get_absolute_url()
        assert url == f"/vendor/{vendor.id}/"


class TestProductModel:
    def test__str_(self, product):
        assert product.__str__() == product.name
        assert str(product) == product.name

    def test_get_absolute_url(self, product):
        url = product.get_absolute_url()
        assert url == f"/product/{product.id}/"

    def test_available_manager(self):
        """Testing available queryset itens"""
        ProductFactory(is_available=True)
        ProductFactory(is_available=False)

        assert len(Product.objects.all()) == 2
        assert len(Product.available.all()) == 1

        assertQuerysetEqual(
            Product.available.all(),
            Product.objects.filter(is_available=True),
            transform=lambda x: x,
        )
