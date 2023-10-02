from django.urls import path
from . import views
urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("lists", views.ListProfiles.as_view())
]