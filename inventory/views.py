from django.shortcuts import render
from .forms import ProductuploadForm
from inventory.models import Product
from django.shortcuts import redirect
from django.db.models import Q
from .models import Product


#there are class based views and function based views
# Create your views here.
def index(request):
    q = request.GET.get('q')  # Get the search query from the request's GET parameters

    if q:  # Check if there's a search query
        multiple_q = Q(Q(name__icontains=q) | Q(price__icontains=q))
        data = Product.objects.filter(multiple_q)
    else:
        data = Product.objects.all()  # If no search query, retrieve all data

    context = {
        'products': data,
        'q': q,  # Pass the search query to the template
    }



def upload_product(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_product = request.FILES["image"]
        form = ProductuploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductuploadForm()
        
    return render(request, "inventory/product_upload.html", {"form": form})
  
  
  #returns many products 
def products_list(request):
    products = Product.objects.all()
    return render (request, "inventory/products_list.html", {"products": products})
  
  #return a single product 
def  product_detail(request,id):
  product = Product.objects.get(id =id)
  related_products = product.related_products.all()
  return render(request,"inventory/product_detail.html",{"product":product,"related_products":related_products})



def index(request):
  return render(request,"inventory/index.html")


def cart(request):
  return render(request,"inventory/cart.html")


def cart_upload(request):
  return render(request,"cart/cart_upload.html")


def edit_product_view(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        form = ProductuploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail_view", id=id)

    else:  # If request method is GET
        form = ProductuploadForm(instance=product)

    return render(request, "inventory/edit_product.html", {"form": form})









