from django.shortcuts import render, redirect
from .models import Apartment, Room
from .forms import ApartmentForm, RoomForm

# Create your views here.

def create_apartment(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST, request.FILES)
        if form.is_valid():
            apartment = form.save(commit=False)
            apartment.owner = request.user
            apartment.save()
            return redirect('create-post', pk=apartment.pk)
    else:
        form = ApartmentForm()
    return render(request, 'create_apartment.html', {'form': form})

def edit_apartment(request, pk):
    apartment = Apartment.objects.get(pk=pk)
    if request.method == 'POST':
        form = ApartmentForm(request.POST, request.FILES, instance=apartment)
        if form.is_valid():
            form.save()
            return redirect('create_post', pk=apartment.pk)
    else:
        form = ApartmentForm(instance=apartment)
    return render(request, 'edit_apartment.html', {'form': form})

def delete_apartment(request, pk):
    apartment = Apartment.objects.get(pk=pk)
    if request.method == 'POST':
        apartment.delete()
        return redirect('apartment_list')
    return render(request, 'delete_apartment.html', {'apartment': apartment})

def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.owner = request.user
            room.save()
            return redirect('create_post', pk=room.pk)
    else:
        form = RoomForm()
    return render(request, 'create_room.html', {'form': form})