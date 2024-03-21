from django.shortcuts import render
from .models import FeedBack

# Create your views here.
def index_view(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        
        feed = FeedBack(name=name, email=email, subject=subject, message=message)
        feed.save()
        return render(request, 'index.html', {'message':'Your feedback has been submitted successfully!'})
    return render(request, 'index.html')

def properties_view(request):
    return render(request, 'properties.html')

def property_details_view(request):
    return render(request, 'property_details.html')

def contact_view(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        
        feed = FeedBack(name=name, email=email, subject=subject, message=message)
        feed.save()
        return render(request, 'contact.html', {'message':'Your feedback has been submitted successfully!'})
    return render(request, 'contact.html')