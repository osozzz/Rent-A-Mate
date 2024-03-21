from django.db import models
from django.contrib.auth.models import User
from Renters.models import Apartment, Room

# Create your models here.
class Posts(models.Model):
    PUBLICATION_CHOICES = [
        ('Apartment', 'Apartment'),
        ('Room', 'Room'),
    ]
    
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_type = models.CharField(max_length=10, choices=PUBLICATION_CHOICES)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey('Reviews', on_delete=models.CASCADE, null=True, blank=True)
    avaliability = models.BooleanField(default=True)
    price = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.publication_type == 'Apartment':
            self.room = None
        elif self.publication_type == 'Room':
            self.apartment = None
        super().save(*args, **kwargs)

class Reviews(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)