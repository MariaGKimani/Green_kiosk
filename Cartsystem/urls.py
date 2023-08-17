from django.urls import path
from .views import upload_cart,cart_list,cart_details,edit_cart
urlpatterns = [
    path("cart/upload", upload_cart, name="upload_cart_view"),
    path("cart/list", cart_list, name = "cart_list_view"),
    path("cart/<int:id>/",cart_details, name="cart_details_view"),
    path("cart/edit/<int:id>",edit_cart, name = "edit_cart_view"),
]