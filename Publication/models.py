from django.db import models
from django.contrib.auth.models import User
from Renters.models import Acommodation

# Create your models here.
class Posts(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    acommodation = models.ForeignKey(Acommodation, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey('Reviews', on_delete=models.CASCADE, null=True, blank=True)
    avaliability = models.BooleanField(default=True)
    def __str__(self):
        return str(self.publisher)

class Reviews(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.publisher)
