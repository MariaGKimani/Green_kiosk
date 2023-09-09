from .import views
from .views import customer_upload,customer_list,customer_detail,customer_edit
from django.urls import path

urlpatterns =[
    path("Customer/upload",  customer_upload, name="customer_upload_view"),
    path("Customer/list",  customer_list, name="customer_list_view"),
    path("Customer/<int:id>/",  customer_detail, name="customer_detail_view"),
    path("Customer/edit/<int:id>/",customer_edit,name="customer_edit_view" ),
    # path("Customer/sign", views.signIn, name='sign_upload_view'),
    path("Customer/login", views.logIn, name='login_upload_view'),
]