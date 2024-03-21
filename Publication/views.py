from django.shortcuts import render, redirect
from .models import Apartment
from .forms import ApartmentForm

def create_apartment(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST, request.FILES)
        if form.is_valid():
            apartment = form.save(commit=False)
            apartment.owner = request.user
            apartment.save()
            return redirect('apartment_detail', pk=apartment.pk)
    else:
        form = ApartmentForm()
    return render(request, 'create_apartment.html', {'form': form})

def edit_apartment(request, pk):
    apartment = Apartment.objects.get(pk=pk)
    if request.method == 'POST':
        form = ApartmentForm(request.POST, request.FILES, instance=apartment)
        if form.is_valid():
            form.save()
            return redirect('apartment_detail', pk=apartment.pk)
    else:
        form = ApartmentForm(instance=apartment)
    return render(request, 'edit_apartment.html', {'form': form})

def delete_apartment(request, pk):
    apartment = Apartment.objects.get(pk=pk)
    if request.method == 'POST':
        apartment.delete()
        return redirect('apartment_list')
    return render(request, 'delete_apartment.html', {'apartment': apartment})
