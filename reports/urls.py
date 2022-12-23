from django.urls import path

from .views import auth, landing, profile

urlpatterns = [
    path("", landing.landing, name="landing"),
    path("login/", auth.login, name="login"),
    path("profile/", profile.user_data, name="profile")
]
