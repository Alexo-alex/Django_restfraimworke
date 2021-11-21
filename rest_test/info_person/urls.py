from .views import *
from django.urls import path

urlpatterns = [
    path("person/", PersonListView.as_view()),
    path("person/<int:pk>/", PersonDetailView.as_view()),
    path("company/", CompanyListView.as_view()),
    path("company/<int:pk>/", CompanyDetailView.as_view()),
]
