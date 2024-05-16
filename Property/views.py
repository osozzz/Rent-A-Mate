from django.shortcuts import render
from Publication.models import Posts
from Renters.models import Acommodation 


# Create your views here.

def property_list_view(request):
    posts = Posts.objects.all()
    return render(request, 'properties.html', {'posts':posts})



