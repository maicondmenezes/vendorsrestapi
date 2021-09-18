from rest_framework import serializers
from catalogue.models import Vendor, Product


class ProductSerializer(serializers.ModelSerializer):
    """This class handle with products database records
    to serializer itens and prepare json to rest api consumers
    """

    class Meta:
        model = Product
        fields = ["name", "code", "price"]


class VendorSerializer(serializers.ModelSerializer):
    """This class handle with vendors database records
    to serializer itens and prepare json to rest api consumers
    """

    products = ProductSerializer(many=True)

    class Meta:
        model = Vendor
        fields = ["name", "cnpj", "city", "products"]

    def save_products(self, vendor, products):
        """This method verifies if a item in a list of products at given vendor instance exist
        if False then create a new item or update that item if it already exists"""

        for product in products:
            code = product.pop("code", None)
            if id is None:
                Product.objects.create(vendor=vendor, **product)
            else:
                Product.objects.filter(code=code, vendor=vendor).update(**product)

    def create(self, validated_data):
        """Create a new vendor and a products list if it exist"""

        products = validated_data.pop("products")
        vendor = Vendor.objects.create(**validated_data)

        if len(products):
            self.save_products(vendor, products)

        return vendor

    def update(self, instance, validated_data):
        """Update a vendor and it's products list"""

        products = validated_data.pop("products")
        vendor = super(VendorSerializer, self).update(instance, validated_data)

        if len(products):
            self.save_products(vendor, products)
        return vendor
