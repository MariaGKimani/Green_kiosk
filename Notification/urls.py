from django.urls import path
from .views import notification_list, add_notification, notification_details, notification_edit
urlpatterns = [
    path("notification/list", notification_list, name="notification_list_view"),
    path("notification/add", add_notification,name="add_notification_view"),
    path("notification/<int:id>/", notification_details, name="notification_details_view"),
    path("notification/edit/<int:id>/", notification_edit, name="notification_edit_view"),
]

