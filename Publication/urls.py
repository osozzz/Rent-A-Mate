from django.urls import path
from Publication import views as PubliViews

urlpatterns = [
    path("create-post/", PubliViews.create_post, name="create-post"),
    path("post/", PubliViews.create_review_view, name="create-review"),
]