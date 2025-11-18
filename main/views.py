from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import requests
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
from django.utils.html import strip_tags
import json

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
    """Return a plain JSON array of products for Flutter consumption.

    Each item contains: id, name, price, description, thumbnail, category,
    is_featured, owner.
    """
    products = Product.objects.all()
    data = []
    for p in products:
        data.append({
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'thumbnail': p.thumbnail,
            'category': p.category,
            'is_featured': p.is_featured,
            'owner': p.owner.username if p.owner else None,
        })
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json_by_id(request, id):
    p = get_object_or_404(Product, pk=id)
    data = {
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'description': p.description,
        'thumbnail': p.thumbnail,
        'category': p.category,
        'is_featured': p.is_featured,
        'owner': p.owner.username if p.owner else None,
    }
    return JsonResponse(data)


def proxy_image(request):
    """Fetch an external image and return it through this server to avoid CORS issues.

    Expects query parameter `url` with the image URL.
    """
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)

    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type', 'image/jpeg')
        return HttpResponse(response.content, content_type=content_type)
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)


def api_products(request):
    """Return JSON list of products. Use `?mine=1` to filter to authenticated user's products.

    This endpoint returns a plain array of product objects suitable for Flutter.
    """
    """
    Mengembalikan daftar produk dalam format JSON datar (Flat JSON).
    Cocok untuk Flutter agar tidak perlu parsing 'fields' dan 'pk' terpisah.
    """
    products = Product.objects.all()
    mine = request.GET.get('mine')
    
    # 1. Logic Filter Produk Milik Sendiri
    if mine == '1' and request.user.is_authenticated:
        products = products.filter(owner=request.user)
    
    # 2. Logic Filter Pencarian (opsional, tapi bagus dipertahankan)
    q = request.GET.get('q')
    if q:
        products = products.filter(name__icontains=q)

    # Jika ingin filter produk milik user sendiri (opsional)
    # if request.user.is_authenticated:
    #     products = products.filter(owner=request.user)

    data = []
    for p in products:
        data.append({
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'thumbnail': p.thumbnail,
            'category': p.category,
            'is_featured': p.is_featured,
            'owner': p.owner.username if p.owner else "Unknown",
        })
    return JsonResponse(data, safe=False)


def api_product_detail(request, id):
    p = get_object_or_404(Product, pk=id)
    data = {
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'description': p.description,
        'thumbnail': p.thumbnail,
        'category': p.category,
        'is_featured': p.is_featured,
        'owner': p.owner.username if p.owner else None,
    }
    return JsonResponse(data)

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

@csrf_exempt
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


@csrf_exempt
def create_product_flutter(request):
    """
    Menerima data JSON dari Flutter dan membuat Product baru.
    """
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'error', 'message': 'Authentication required.'}, status=401)
        
        try:
            data = json.loads(request.body.decode('utf-8'))
            
            # Validasi field wajib
            name = data.get('name')
            price = data.get('price')
            if not name or price is None:
                 return JsonResponse({'status': 'error', 'message': 'Name and Price are required.'}, status=400)

            new_product = Product.objects.create(
                owner=request.user,
                name=name,
                price=int(price),
                description=data.get('description', ''),
                category=data.get('category', 'boots'),
                thumbnail=data.get('thumbnail', ''),
                is_featured=data.get('is_featured', False),
            )
            new_product.save()

            return JsonResponse({'status': 'success', 'message': 'Product created successfully!'}, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)