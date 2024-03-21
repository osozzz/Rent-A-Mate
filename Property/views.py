from django.shortcuts import render

# Create your views here.

def Property_list_view(request):
    return render(request, 'property_list.html')