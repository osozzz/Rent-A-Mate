from django.urls import path
from Index import views as indexViews

urlpatterns = [
    path("", indexViews.index_view, name="main"),
]
