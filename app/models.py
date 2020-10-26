from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),

    )
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORY)
    description = models.TextField(blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivering', 'Out for delivering'),
        ('Delivered', 'Delivered'),
    )
    custom = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='c_order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='p_order')
    time_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS)
