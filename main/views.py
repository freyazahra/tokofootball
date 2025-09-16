from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm

def home(request):
    products = Product.objects.all()
    context = {
        "app_name": "Kalcer Shop",
        "student_name": "Freya Zahra",   
        "student_class": "PBP F",  
        "products": products,     
    }
    return render(request, "main.html", context) 

#render = cara Django “mengirim” variabel itu ke file HTML (main.html).
#jadi intinya di views ini kita kayak simpan varibel buat bisa di aksem di main.html

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:show_main")  # balik ke main setelah tambah produk
    else:
        form = ProductForm()
    return render(request, "product_form.html", {"form": form})

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