from django.urls import path
from Renters import views as RenterViews

urlpatterns = [
    path('create-acommodation/', RenterViews.create_acommodation, name='create_acommodation'),
    path('edit/<int:pk>/', RenterViews.edit_acommodation, name='edit_acommodation'),
    path('delete/<int:pk>/', RenterViews.delete_acommodation, name='delete_acommodation'),
]
