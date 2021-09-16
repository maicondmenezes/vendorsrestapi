from django.urls import path
from catalogue.views import ProductDetailView, ProductListView

app_name = "catalogue"

urlpatterns = [
    path("", ProductListView.as_view, name="list"),
    path("product/<int:id>", ProductDetailView.as_view, name="product_detail"),
    path("vendor/<int:id>", ProductListView.as_view, name="list_by_vendor"),
]
