import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Product, CartItem
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django import forms
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages

stripe.api_key = settings.STRIPE_SECRET_KEY

class CheckoutForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    address1 = forms.CharField(label='Address line 1', max_length=255)
    address2 = forms.CharField(label='Address line 2', max_length=255, required=False)
    city = forms.CharField(max_length=100)
    zip_code = forms.CharField(label='Zip Code', max_length=12)
    country = forms.CharField(max_length=100)
    card_number = forms.CharField(label='Card Number', max_length=16)
    card_expiry_month = forms.IntegerField(label='Expiration Month', min_value=1, max_value=12)
    card_expiry_year = forms.IntegerField(label='Expiration Year', min_value=2021, max_value=2030)
    card_cvc = forms.CharField(label='CVC', max_length=3)

def home(request):
    recent_date = timezone.now() - timedelta(days=30)
    new_products = Product.objects.filter(added_date__gte=recent_date, is_new=True)
    return render(request, 'main/home.html', {'new_products': new_products})

def dewalt_products(request):
    products = Product.objects.filter(brand='Dewalt')
    return render(request, 'main/dewalt_products.html', {'products': products})

def makita_products(request):
    products = Product.objects.filter(brand='Makita')
    return render(request, 'main/makita_products.html', {'products': products})

def ryobi_products(request):
    products = Product.objects.filter(brand='Ryobi')
    return render(request, 'main/ryobi_products.html', {'products': products})

def milwaukee_products(request):
    products = Product.objects.filter(brand='Milwaukee')
    return render(request, 'main/milwaukee_products.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    cart_item, created = CartItem.objects.get_or_create(product=product, user=user, defaults={'quantity': 1})
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.add_message(request, messages.INFO, 'Item added to cart successfully!')
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    messages.add_message(request, messages.SUCCESS, 'Product removed from cart.')
    return redirect('cart_detail')

def cart_detail(request):
    if not request.user.is_authenticated:
        return render(request, 'main/cart_detail.html', {'cart_items': []})
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'main/cart_detail.html', {'cart_items': cart_items})

def checkout_view(request):
    form = CheckoutForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # Assume checkout logic is processed here
        messages.add_message(request, messages.SUCCESS, 'Checkout successful.')
        return redirect('order_confirmation')  # This should point to an existing view that handles order confirmation
    return render(request, 'main/checkout.html', {'form': form})
