from rest_framework import serializers
from catalogue.models import Vendor, Product


class ProductSerializer(serializers.ModelSerializer):
    """This class handle with vendors database records
    to serializer and deserializer itens and prepare json to rest api consumers
    """

    class Meta:
        model = Product
        fields = ["name", "code", "price"]


class VendorSerializer(serializers.ModelSerializer):
    """This class handle with vendors database records
    to serializer and deserializer itens and prepare json to rest api consumers
    """

    products = ProductSerializer(many=True)

    class Meta:
        model = Vendor
        fields = ["name", "cnpj", "city", "products"]

    def create(self, validated_data):
        products_data = validated_data.pop("products")
        vendor = Vendor.objects.create(**validated_data)
        for product_data in products_data:
            Product.objects.create(vendor=vendor, **product_data)
        return vendor

    def update(self, validated_data):
        products_data = validated_data.pop("products")
        vendor = Vendor.objects.update(**validated_data)
        for product_data in products_data:
            Product.objects.update(vendor=vendor, **product_data)
        return vendor
