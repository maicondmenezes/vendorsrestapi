from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from catalogue.models import Vendor, Product
from catalogue.serializers import VendorSerializer, ProductSerializer


class ProductViewset(viewsets.ModelViewSet):
    """Defines a set of CRUD views to handle with data repesentation of products dabatase objects."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"


class VendorViewset(viewsets.ModelViewSet):
    """Defines a set of CRUD views to handle with data repesentation of vendors dabatase objects."""

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"
