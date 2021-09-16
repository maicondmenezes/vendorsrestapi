from rest_framework import viewsets
from catalogue.models import Vendor, Product
from catalogue.serializers import VendorSerializer, ProductSerializer


class VendorViewset(viewsets.ModelViewSet):
    """Conjunto de seleções de dados para interagir com a api rest gerada pelo django-rest-framework."""

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class ProductViewset(viewsets.ModelViewSet):
    """Conjunto de seleções de dados para interagir com a api rest gerada pelo django-rest-framework."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
