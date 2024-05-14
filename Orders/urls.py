from django.urls import path
from Orders import views as orderViews

urlpatterns = [
    path('create_order/<int:acommodation_id>/<int:post_id>/', orderViews.create_order, name='create_order'),
    path('user/<int:user_id>/orders/<str:filter_by>/', orderViews.orders_view, name='user_orders'),
]
