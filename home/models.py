from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Magazin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100) 
    image = models.ImageField(upload_to='images/%y/%m/%d' , default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    magazin = models.ForeignKey(Magazin, default='',on_delete=models.CASCADE)
    number_of_items = models.IntegerField(default=0)
    def __str__(self):
        return self.name
        

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - Quantity: {self.quantity}"
    

class NumeroUrgence(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    number = models.CharField(max_length=20, default=0)

    def __str__(self):
        return f"{self.name} - {self.number}"
    


class Kit(models.Model):
    id = models.AutoField(primary_key=True)
    magazin = models.ForeignKey(Magazin, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Default Kit Name')
    item1 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='kit_item1', null=True)
    item2 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='kit_item2', null=True)
    item3 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='kit_item3', null=True)
    item4 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='kit_item4', null=True)
    item5 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='kit_item5', null=True)
    item6 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='kit_item6', null=True)
    purchase_count = models.IntegerField(default=0)  

    def __str__(self):
        return f"{self.name} - Purchase Count: {self.purchase_count}"
    
    def total_price(self):
        total_price = 0
        if self.item1:
            total_price += self.item1.price
        if self.item2:
            total_price += self.item2.price
        if self.item3:
            total_price += self.item3.price
        if self.item4:
            total_price += self.item4.price
        if self.item5:
            total_price += self.item5.price
        if self.item6:
            total_price += self.item6.price
        return total_price
    

class FavoriteKit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.user.username}'s favorite kit: {self.kit.name}"