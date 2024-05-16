from django.urls import path, include
from Core import views as coreViews
from FeedBack import views as FeedBViews
from Publication import views as PubliViews
from Property import views as propViews
from Renters import views as RenterViews
from Renters.models import Acommodation
from Renters.forms import AcommodationForm

urlpatterns = [
    path("core/", coreViews.core_view, name="core"),
    path("post/", coreViews.index_view, name="index"),
    path("properties/", coreViews.properties_view, name="properties"),
    path("contact/", FeedBViews.contact_view, name='contact'),
    path("create-post/<int:acommodation_id>/", PubliViews.create_post, name="create-post"),
    path("post/<int:post_id>/", PubliViews.property_details_view, name="publi-and-review"),
    path("property-list/", propViews.property_list_view, name="prop"),
    
    path('create-acommodation/', RenterViews.create_acommodation, name='create_acommodation'),
    
    
    
]
