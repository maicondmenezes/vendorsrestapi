from django.urls import path
from catalogue.views import ProductDetailView, ProductListView

app_name = "catalogue"

urlpatterns = [
    path("product/", ProductListView.as_view, name="product_detail"),
    path("vendor/<int:id>", ProductListView.as_view, name="list_by_vendor"),
]
