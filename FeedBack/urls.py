from django.urls import path
from FeedBack import views as FeedBviews

urlpatterns = [
    path('contact/', FeedBviews.contact_view, name='contact'),
]
