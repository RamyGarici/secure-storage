from .views import FileUploadView, FileView
from django.urls import path


urlpatterns = [
    path("upload/", FileUploadView.as_view(), name="upload"),
    path("", FileView.as_view(), name="file-list"),
    path("<int:id>/", FileView.as_view(),name="file-delete")


]
