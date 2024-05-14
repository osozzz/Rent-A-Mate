from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Acommodation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    PUBLICATION_CHOICES = [
        ('Apartment', 'Apartment'),
        ('Room', 'Room'),
        ('Studio', 'Studio'),
        ('House', 'House'),
    ]
    typo = models.CharField(max_length=10, choices=PUBLICATION_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    parking_slots = models.IntegerField()
    area_m2 = models.IntegerField()
    image = models.ImageField(upload_to='static/media/Utility/Public/apartment_images-uploaded/')
    times_rented = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.title)
