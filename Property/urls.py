from django.urls import path
from Property import views as propViews

urlpatterns = [
    path("properties/", propViews.property_list_view, name="prop"),
]
