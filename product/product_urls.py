from django.urls import path
from product import views

urlpatterns = [
    path("",views.ProductList.as_view(), name="all-products"),
    path("<int:id>/", views.SpecificProductList.as_view(), name="specific-product")
]