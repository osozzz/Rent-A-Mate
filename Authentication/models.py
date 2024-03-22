from django.db import models
from django.contrib.auth.models import User
from Publication.models import Posts

# Create your models here.
class Data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200)
    saved_posts = models.ManyToManyField(Posts, related_name='saved_by_users')  # Relación Many-to-Many con Posts
    order_history = models.JSONField(default=list)
    sale_list = models.JSONField(default=list)
    payment_info = models.JSONField(default=list)