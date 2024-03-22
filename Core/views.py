from django.shortcuts import render
from Publication.models import Posts

# Create your views here.
def core_view(request):
    posts = Posts.objects.all()
    return render(request, 'core.html', {'posts': posts})