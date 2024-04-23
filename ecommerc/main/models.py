from django.conf import settings
from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/')
    brand = models.CharField(max_length=100)
    added_date = models.DateTimeField(default=timezone.now)  # Automatically sets to the current date/time when a product is created
    is_new = models.BooleanField(default=False)  # Manually set to True for new products

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='cart_items'
    )
    session_key = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def total_price(self):
        return self.quantity * self.product.price
