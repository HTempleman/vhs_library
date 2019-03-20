from django.urls import path
from vhs_library import views

urlpatterns = [
    path('movies/', views.MovieUpdate.as_view()),
]