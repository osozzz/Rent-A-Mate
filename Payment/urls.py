from django.urls import path
from Payment import views as PayViews

urlpatterns = [
    path("create-card/", PayViews.create_card, name="create-card"),
    path("cards/", PayViews.cards_list, name="cards"),
]
