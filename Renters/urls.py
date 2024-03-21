from django.urls import path
from . import views

urlpatterns = [
    path('create-apartment/', views.create_apartment, name='create_apartment'),
    path('edit/<int:pk>/', views.edit_apartment, name='edit_apartment'),
    path('delete/<int:pk>/', views.delete_apartment, name='delete_apartment'),
    path('create-room/', views.create_room, name='create_room'),
]
