from django.urls import path

#function that exist urls


# from .import views
from .views import upload_product,product_detail,products_list,edit_product_view
from .import views

urlpatterns = [
    path("products/upload", upload_product, name="product_upload_view"),
    path("products/list", products_list, name = "products_list_view"),
    path("products/<int:id>/",product_detail, name="product_detail_view"),
    path("products/edit/<int:id>/", edit_product_view, name = "product_edit_view"),
    path('carts/upload/', views.cart_upload, name='cart-upload'),
    path('cart/', views.cart , name='cartt'),
    path('',views.index, name ='index')
]

#from the above you have the path   and the view should go to the upload_product from the views.py and now the path name 95432=