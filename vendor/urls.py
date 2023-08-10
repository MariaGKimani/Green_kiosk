from .views import vendor_upload,vendor_detail,vendor_edit,vendor_list
from .import views
from django.urls import path

urlpatterns = [   
    path("Vendor/upload",  vendor_upload, name="vendor_upload_view"),
    path("Vendor/list", vendor_list, name = "vendor_list_view"),
    path("Vendor/<int:id>/",  vendor_detail, name="vendor_detail_view"),
    path("Vendor/edit/<int:id>/",vendor_edit,name="vendor_edit_view" )
    
]