# main/urls.py
from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    # Main pages
    path('', views.home, name='show_main'),
    
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    # Product CRUD (Original - you can keep these or remove them)
    path('create-product/', views.create_product, name='create_product'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('edit-product/<int:id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:id>/', views.delete_product, name='delete_product'),
    
    # AJAX endpoints for modals (NEW)
    path('create-product-ajax/', views.create_product_ajax, name='create_product_ajax'),
    path('edit-product-ajax/<int:id>/', views.edit_product_ajax, name='edit_product_ajax'),
    path('product-detail-ajax/<int:id>/', views.product_detail_ajax, name='product_detail_ajax'),
    path('delete-product-ajax/<int:id>/', views.delete_product_ajax, name='delete_product_ajax'),
    
    # Data serialization
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),
    
    # Search
    path('search/', views.search_product, name='search_product'),
]