from django.db import models
from django.contrib.auth.models import User
from Publication.models import Posts
from Payment.models import Card

# Create your models here.
class Data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200)
    saved_posts = models.ManyToManyField(Posts, related_name='saved_by_users')
    payment_info = models.ManyToManyField(Card, related_name='users_cards')
