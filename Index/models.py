from django.db import models

# Create your models here.
class FeedBack(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
    
    #def __str__(self) -> str:
        #return super().__str__()