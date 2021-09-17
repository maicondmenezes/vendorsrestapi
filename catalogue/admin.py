from django.contrib import admin

from catalogue.models import Vendor, Product


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ["name", "cnpj", "created", "modified"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "vendor",
        "name",
        "code",
        "price",
        "is_available",
        "created",
        "modified",
    ]
    list_filter = ["is_available", "created", "modified", "vendor"]
    list_editable = ["price", "is_available"]
