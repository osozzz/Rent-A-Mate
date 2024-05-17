from django.urls import path
from Orders import views as orderViews

urlpatterns = [
    path('create_order/<int:post_id>/', orderViews.create_order, name='create_order'),
    path('orders/<str:filter_by>/', orderViews.orders_view, name='orders'),
]
