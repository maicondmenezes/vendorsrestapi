"""vendorsrestapi URL Configuration

The `urlpatterns` list routes URLs to views. 
Api objects are routed with routers of django rest framework
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from catalogue.views import VendorViewset, ProductViewset

router = routers.DefaultRouter()
router.register(r"vendor", VendorViewset, basename="vendor")
router.register(r"product", ProductViewset, basename="product")

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    path("catalogue/", include((router.urls, "catalogue"), namespace="catalogue")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
