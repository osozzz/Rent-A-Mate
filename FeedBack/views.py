from django.shortcuts import render
from .models import FeedBack

# Create your views here.
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
