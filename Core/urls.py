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
    path("", coreViews.index_view, name="index") 
]
