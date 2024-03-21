from django.db import models
from django.contrib.auth.models import User
from Publication.models import Posts

class Card(models.Model):
    CARD_TYPE_CHOICES = [
        ('debit', 'Débito'),
        ('credit', 'Crédito'),
    ]
    
    card_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards')
    card_number = models.CharField(max_length=16)
    card_expire = models.DateField()
    card_cvc = models.CharField(max_length=4)
    card_type = models.CharField(max_length=10, choices=CARD_TYPE_CHOICES)

    def __str__(self):
        return f'{self.card_owner.username} - {self.card_number}'

class Order(models.Model):
    payment_method = models.ForeignKey(Card, on_delete=models.CASCADE)
    publication = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_period_start = models.DateField()
    rental_period_end = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calcular la cantidad total basada en el precio de la publicación y la duración del arriendo
        rental_months = (self.rental_period_end - self.rental_period_start).days // 30
        self.total_amount = self.publication.price * rental_months
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order {self.id} - User: {self.user.username}'