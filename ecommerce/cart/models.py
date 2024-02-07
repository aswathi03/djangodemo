from django.db import models
from shop.models import product
from django.contrib.auth.models import User


class Cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       # return self.user.name
        return self.product.name

    def subtotal(self):
        return self.quantity*self.product.price

class order(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    no_of_items=models.IntegerField()
    address=models.TextField()
    phone = models.IntegerField()
    order_status=models.CharField(max_length=20,default="pending")
    delivery_status=models.CharField(max_length=20,default="pending")
    ordered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      # return self.user.username
        return self.product.name

class account(models.Model):
    acctnum=models.IntegerField()
    accttype=models.CharField(max_length=20)
    amount=models.IntegerField()

    def __str__(self):
        return str(self.acctnum)




