from django.shortcuts import render
from django.core.paginator import Paginator
from Publication.models import Posts
from Renters.models import Acommodation

# Create your views here.

def property_list_view(request, filter_type=None):
    if filter_type == "Apartment":
        posts = Posts.objects.filter(acommodation.typo=="Apartment")
    elif filter_type == "Room":
        posts = Posts.objects.filter(acommodation.typo=="Room")
    elif filter_type == "House":
        posts = Posts.objects.filter(acommodation.typo=="House")
    elif filter_type == "Studio":
        posts = Posts.objects.filter(acommodation.typo=="Studio")
    else:
        posts = Posts.objects.all()
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'properties.html', {'posts': posts, 'page_obj':page_obj})
