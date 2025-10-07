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
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# ============================================
# AJAX VIEWS FOR MODALS
# ============================================

@login_required(login_url='/login')
def create_product_ajax(request):
    if request.method == 'GET':
        # Render the form template
        html = render_to_string('product_form_modal.html', {
            'form': ProductForm(),
            'action_url': '/create-product-ajax/',
            'is_edit': False
        }, request=request)
        return JsonResponse({'html': html}, safe=False)
    
    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user  # Set owner to logged-in user
            product.save()
            return JsonResponse({
                'success': True,
                'message': 'Product added successfully!',
                'product_id': product.id
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors,
                'message': 'Please correct the errors below.'
            })

@login_required(login_url='/login')
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    
    if request.method == 'GET':
        form = ProductForm(instance=product)
        html = render_to_string('product_form_modal.html', {
            'form': form,
            'action_url': f'/edit-product-ajax/{id}/',
            'is_edit': True,
            'product': product
        }, request=request)
        return JsonResponse({'html': html}, safe=False)
    
    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'success': True,
                'message': 'Product updated successfully!',
                'product_id': product.id
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors,
                'message': 'Please correct the errors below.'
            })

@login_required(login_url='/login')
def product_detail_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    html = render_to_string('product_detail_modal.html', {
        'product': product
    }, request=request)
    return JsonResponse({'html': html}, safe=False)

@login_required(login_url='/login')
@require_POST
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return JsonResponse({
            'success': True,
            'message': 'Product deleted successfully!'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)

# ============================================
# EXISTING VIEWS (Keep these)
# ============================================

@login_required(login_url='/login')
def home(request):
    filter_type = request.GET.get("filter", "all")
    query = request.GET.get('q')

    if filter_type == "my":
        products = Product.objects.filter(owner=request.user)
    else:
        products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    context = {
        "app_name": "Kalcer Shop",
        "student_name": "Freya Zahra",   
        "student_class": "PBP F",  
        "products": products,
        "last_login": request.COOKIES.get("last_login", "Never"),
        "queries": query,
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)  
        product.owner = request.user
        product.save()
        return redirect("main:show_main")

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
      form = AuthenticationForm(data=request.POST)

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

@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)  

    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")

    context = {
        "form": form,
    }
    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def search_product(request):
    query = request.GET.get('q')
    products = Product.objects.all()
    if query:
        products = products.filter(name__icontains=query)
    return render(request, 'search_results.html', {'products': products, 'query': query})