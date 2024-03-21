from django.urls import path
from Index import views as indexViews

urlpatterns = [
    path("", indexViews.index_view, name="index"),
    path("properties/", indexViews.properties_view, name="properties"),
    path("property-details/", indexViews.property_details_view, name="property-details"),
    path("contact/", indexViews.contact_view, name="contact"),
]
