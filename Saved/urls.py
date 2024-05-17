from django.urls import path
from Saved import views as savedViews

urlpatterns = [
    path("saved/", savedViews.saved_list_view, name="saved")
]
