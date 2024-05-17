from django.urls import path
from Allays import views as allayViews

urlpatterns = [
    path("productos-aliados/", allayViews.productos_aliados, name="aliados"),
]
