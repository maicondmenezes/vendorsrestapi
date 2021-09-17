import factory
import factory.fuzzy
from random import randint as fuzzyInt

from catalogue.models import Vendor, Product


class VendorFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    cnpj = factory.Faker("cnpj", locale="pt_BR")

    class Meta:
        model = Vendor


class ProductFactory(factory.django.DjangoModelFactory):
    vendor = factory.SubFactory(VendorFactory)
    name = factory.fuzzy.FuzzyText()
    code = factory.fuzzy.FuzzyText()
    price = factory.fuzzy.FuzzyDecimal(3.5, 9999.99)
    is_available = factory.Faker("pybool")

    class Meta:
        model = Product
