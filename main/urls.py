from django.urls import path
from main.views import home, show_xml, show_json, show_xml_by_id, show_json_by_id,  create_product, product_detail

app_name = 'main'

urlpatterns = [
    path('', home, name='show_main'),
    path("add/", create_product, name="create_product"),
    path("detail/<int:id>/", product_detail, name="product_detail"),

    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]