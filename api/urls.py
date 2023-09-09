from django.urls import path

from .views import CustomerDetailView, CustomerListView,ProductListView,ProductDetailView,OrderDetailView,OrderListView,AddToCartView



urlpatterns =[
    path ("Customer/",CustomerListView.as_view(), name = "customer_list_view"),
    path("Customer/<int:id>/",CustomerDetailView.as_view(), name = "customer_detail_view"),
    path("Product/",ProductListView.as_view(),name = "product_list_view"),
    path("Product/<int:id>/",ProductDetailView.as_view(), name = "product_detail_view"),
    path("Order/",OrderListView.as_view(),name="order_list_view"),
    path("Order/<int:id>/",OrderDetailView.as_view(),name="order_detail.view"),
    path("add_to_cart",AddToCartView.as_view(),name = "add_to_cart")
]