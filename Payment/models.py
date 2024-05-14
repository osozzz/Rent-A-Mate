from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    CARD_TYPE_CHOICES = [
        ('debit', 'Débito'),
        ('credit', 'Crédito'),
    ]
    card_name = models.CharField(max_length=16, primary_key=True, unique=True, blank=True)
    card_number = models.CharField(max_length=16)
    card_expire = models.DateField()
    card_cvc = models.CharField(max_length=4)
    card_type = models.CharField(max_length=10, choices=CARD_TYPE_CHOICES)

    def __str__(self):
        return f'{self.card_name}'
