from django.shortcuts import render

# Create your views here.

def property_list_view(request):
    return render(request, 'properties.html')
