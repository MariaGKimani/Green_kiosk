from django.shortcuts import render
# from django.contrib.auth.forms import AuthenticationForm, UserCreationsForm
from .forms import CustomeruploadForm
from .models import Customer
from django.shortcuts import redirect

# Create your views here.

def customer_upload(request):                      #the request represents a http request
    if request.method == 'POST':
        # uploaded_customer = request.FILES["image"]
        form = CustomeruploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CustomeruploadForm()
        
    return render(request, "customer/customer_upload.html", {"form": form})

def customer_list(request):
    customers = Customer.objects.all()
    return render (request, "customer/customer_list.html", {"customers": customers})
    
def  customer_detail(request,id):
  customerr = Customer.objects.get(id =id)
  return render(request,"customer/customer_detail.html",{"customer":customerr})

    

def customer_edit(request, id):
    customer = Customer.objects.get(id=id)

    if request.method == 'POST':
        form = CustomeruploadForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_detail_view", id=id)

    else:  # If request method is GET
        form = CustomeruploadForm(instance=customer)

    return render(request, "customer/edit_customer.html", {"form": form})


  
def signIn (request):
    if request.method == 'POST':
        form = CustomeruploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form = CustomeruploadForm()
        return redirect(request,"customer/signIn.html", {"form":form})
  
  
def logIn (request):
    return render(request,"customer/login.html")
    