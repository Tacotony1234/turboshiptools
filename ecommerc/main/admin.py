from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'image')

admin.site.register(Product, ProductAdmin)
