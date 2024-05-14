from django.urls import path
from Core import views as coreViews

urlpatterns = [
    path("core/", coreViews.core_view, name="core"),
    path("", coreViews.index_view, name="index"),
    path("properties/", coreViews.properties_view, name="properties"),
]
