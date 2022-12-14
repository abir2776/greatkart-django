from email.policy import default
from django.db import models
from store.models import Product

# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    cart_id = models.CharField(max_length=250,blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart    = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.ImageField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product
