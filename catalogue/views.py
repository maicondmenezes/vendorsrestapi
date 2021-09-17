from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from catalogue.models import Vendor, Product
from catalogue.serializers import VendorSerializer, ProductSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"


class VendorViewset(viewsets.ModelViewSet):
    """Conjunto de seleções de dados para interagir com a api rest gerada pelo django-rest-framework."""

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"
