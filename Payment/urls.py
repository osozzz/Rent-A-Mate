from django.urls import path
from Payment import views as PayViews

urlpatterns = [
    path("create-card/", PayViews.create_card, name="create-card"),
    path("create-order/", PayViews.create_order, name="create-order"),
    path("orders/", PayViews.order_list, name="orders"),
]
