from django.shortcuts import render
from Publication.models import Posts

# Create your views here.
def core_view(request):
    posts = Posts.objects.all()
    return render(request, 'base.html', {'posts': posts})

def index_view(request):
    return render(request, 'index.html')

def properties_view(request):
    return render(request, 'properties.html')
