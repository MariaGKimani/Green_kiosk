from django.shortcuts import render,redirect
from  .forms import CartuploadForm
from Cartsystem.models import Cart
# Create your views here.
def upload_cart(request):
    if request.method == 'POST':
        form = CartuploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CartuploadForm()
    return render(request, "cart/upload_cart.html", {"form": form})

def cart_list(request):
    carts = Cart.objects.all()
    return render (request, "cart/cart_list.html", {"carts": carts})

def  cart_details(request,id):
  cart = Cart.objects.get(id =id)
  return render(request,"cart/cart_detail.html",{"cart": cart})

def edit_cart(request, id):
    cart = Cart.objects.get(id=id)
    if request.method == "POST":
        form = CartuploadForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return redirect("cart_detail_view", id=cart)
    else:
        form = CartuploadForm(instance=cart)
    return render(request, "cart/edit_cart.html", {"cart": cart})