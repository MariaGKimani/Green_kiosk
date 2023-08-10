from django.shortcuts import render
from .forms import OrderuploadForm
from .models import  Order
from django.shortcuts import redirect

# Create your views here.

def order_upload(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_product = request.FILES["image"]
        form = OrderuploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = OrderuploadForm()
        
    return render(request, "order/order_upload.html", {"form": form})

def  order_detail(request,id):
    order = Order.objects.get(id = id) 
    return render(request,"order/order_detail.html",{"order":order})

def order_list(request):
    orders = Order.objects.all()
    return render (request, "order/order_list.html", {"orders": orders})


def order_edit(request, id):
    order = Order.objects.get(id=id)

    if request.method == 'POST':
        form = OrderuploadForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("order_edit_view", id=id)

    else:  # If request method is GET
        form =OrderuploadForm(instance=order)
        return render(request, "order/edit_order.html", {"form": form})



    