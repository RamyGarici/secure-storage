from .views import FileUploadView, FileView, FileDownloadView
from django.urls import path


urlpatterns = [
    path("upload/", FileUploadView.as_view(), name="upload"),
    path("", FileView.as_view(), name="file-list"),
    path("<int:id>/", FileView.as_view(),name="file-delete"),
    path("<int:id>/download/",FileDownloadView.as_view(), name = "file-download")


]
