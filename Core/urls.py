from django.urls import path
from Core import views as coreViews

urlpatterns = [
    path("core/", coreViews.core_view, name="core"),
]