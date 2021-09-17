import pytest

from catalogue.tests.factories import VendorFactory, ProductFactory


@pytest.fixture
def vendor():
    return VendorFactory()


@pytest.fixture
def product():
    return ProductFactory()
