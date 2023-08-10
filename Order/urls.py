from .views import order_upload,order_detail,order_edit,order_list
from .import views
from django.urls import path


urlpatterns = [  
    path("Order/upload",  order_upload, name="order_upload_view"),
    path("Order/list", order_list, name = "order1_list_view"),
    path("Order/<int:id>/",  order_detail, name="order_detail_view"),
    path("Order/edit/<int:id>/",order_edit,name="order_edit_view" ),
    
]