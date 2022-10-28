from django.contrib import admin
from django.urls import include, path
from .views import ProductCategoryListView, MakerListView, ProductsListView

app_name = "products"

urlpatterns = [
    path("", ProductsListView.as_view(), name="products-list"),
    path("categories", ProductCategoryListView.as_view(), name="categories-list"),
    path("makers", MakerListView.as_view(), name="makers-list"),
]
