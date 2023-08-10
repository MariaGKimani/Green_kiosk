from django.shortcuts import render
from .forms import VendoruploadForm
from .models import Vendor
from django.shortcuts import redirect

# Create your views here.

def vendor_upload(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_vendor = request.FILES["image"]
        form = VendoruploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = VendoruploadForm()
    return render(request, "vendor/vendor_upload.html", {"form": form})

def  vendor_detail(request,id):
    vendorr = Vendor.objects.get(id = id) 
    return render(request,"vendor/vendor_detail.html",{"vendor":vendorr})

def vendor_list(request):
    vendor = Vendor.objects.all()
    return render (request, "vendor/vendor_list.html",{"vendor ": vendor})

def vendor_edit(request, id):
    vendor = Vendor.objects.get(id=id)

    if request.method == 'POST':
        form = VendoruploadForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect("vendor_edit_view", id=id)

    else: 
        # If request method is GET
        form =VendoruploadForm(instance=vendor)
        return render(request, "vendor/edit_vendor.html", {"form": form})
    

