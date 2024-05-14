from django.db import models
from django.contrib.auth.models import User
from Renters.models import Acommodation
from Payment.models import Card

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ('On Hold', 'On Hold'),
        ('Approve', 'Approve'),
        ('Denied', 'Denied'),
    ]
    PAYMENT_CHOICES = [
        ('Card', 'Card'),
        ('PSE', 'PSE'),
        ('PayPal', 'PayPal'),
    ]
    acommodation = models.ForeignKey(Acommodation, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='orders_as_seller', on_delete=models.CASCADE)
    shopper = models.ForeignKey(User, related_name='orders_as_shopper', on_delete=models.CASCADE)
    rental_period_start = models.DateField()
    rental_period_end = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    card_selected = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    payment_status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Order {self.id} - User: {self.shopper.username}'
