from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')
def home(request):
    filter_type = request.GET.get("filter", "all")   # baca query param

    if filter_type == "my":
        products = Product.objects.filter(owner=request.user)   # produk milik user login
    else:
        products = Product.objects.all()   # semua produk

    context = {
        "app_name": "Kalcer Shop",
        "student_name": "Freya Zahra",   
        "student_class": "PBP F",  
        "products": products,
        "last_login": request.COOKIES.get("last_login", "Never"),
    }
    return render(request, "main.html", context)

#render = cara Django “mengirim” variabel itu ke file HTML (main.html).
#jadi intinya di views ini kita kayak simpan varibel buat bisa di aksem di main.html

def create_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)  
        product.owner = request.user       # isi owner dengan user yang login
        product.save()                     # baru simpan ke DB
        return redirect("main:show_main")  # balik ke main setelah tambah produk

    return render(request, "product_form.html", {"form": form})

@login_required(login_url='/login')
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})

def show_xml(request):
    data = Product.objects.all()
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    json_data = serializers.serialize("json", data)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, id):
    obj = get_object_or_404(Product, pk=id)
    json_data = serializers.serialize("json", [obj])
    return HttpResponse(json_data, content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST) #nuat check sebelumnya ada akun nya

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response