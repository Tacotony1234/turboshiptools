from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('dewalt/', views.dewalt_products, name='dewalt_products'),
    path('makita/', views.makita_products, name='makita_products'),
    path('ryobi/', views.ryobi_products, name='ryobi_products'),
    path('milwaukee/', views.milwaukee_products, name='milwaukee_products'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('accounts/', include('django.contrib.auth.urls')),
]
