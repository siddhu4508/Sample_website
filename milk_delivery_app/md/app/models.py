from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_ordered = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField()
    status_choices = [
        ('PENDING', 'Pending'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled')
    ]
    status = models.CharField(
        max_length=20, choices=status_choices, default='PENDING')

    def __str__(self):
        return f'{self.product} - {self.customer}'


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    status_choices = [
        ('IN TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered')
    ]
    status = models.CharField(
        max_length=20, choices=status_choices, default='IN TRANSIT')

    def __str__(self):
        return f'Delivery for {self.order}'


class Subscription(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    frequency_choices = [
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly')
    ]
    frequency = models.CharField(max_length=10, choices=frequency_choices)

    def __str__(self):
        return f'{self.customer} Subscription'
