from django.shortcuts import render , redirect
# Create your views here.
from .forms import NotificationuploadForm
from .models import Notification

def add_notification(request):
    if request.method == "POST":
        form = NotificationuploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = NotificationuploadForm()
    return render(request, "notification/notification_add.html", {"form": form})

def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, "notification/notification_list.html", {"notifications": notifications})

def notification_details(request, id):
    notification = Notification.objects.get(id=id)
    return render(request, "notification/notification_detail.html", {"notification": notification})

def notification_edit(request, id):
    notification = Notification.objects.get(id=id)
    if request.method == "POST":
        form = NotificationuploadForm(request.POST, instance=notification)
        form.is_valid()
        form.save()
        return redirect("notification_details", id=notification.id)
    else:
        form = NotificationuploadForm(instance=notification)
        return render(request, "notification/notification_edit.html", {"form": form})

