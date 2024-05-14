from django.urls import path
from Publication import views as PubliViews

urlpatterns = [
    path("create-post/<int:acommodation_id>/", PubliViews.create_post, name="create-post"),
    path("post/<int:post_id>/", PubliViews.property_details_view, name="publi-and-review"),
]
