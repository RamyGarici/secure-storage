from .views import RegisterView, MeView
from django.urls import path


urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("me", MeView.as_view(), name="me")

]
