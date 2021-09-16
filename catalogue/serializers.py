from rest_framework import serializers
from catalogue.models import Vendor, Product


class VendorSerializer(serializers.ModelSerializer):
    """This class handle with vendors database records
    to serializer and deserializer itens and prepare json to rest api consumers
    """

    class Meta:
        model = Vendor
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """This class handle with vendors database records
    to serializer and deserializer itens and prepare json to rest api consumers
    """

    class Meta:
        model = Product
        fields = "__all__"
