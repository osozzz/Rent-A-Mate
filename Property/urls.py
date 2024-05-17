from django.urls import path
from Property import views as propViews

urlpatterns = [
    path("properties/", propViews.property_list_view, name="all-posts"),
    path('posts/<str:filter_type>/', propViews.property_list_view, name='filter_posts'),
]
