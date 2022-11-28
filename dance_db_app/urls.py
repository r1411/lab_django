from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artist/<int:artist_id>/', views.view_artist, name="view_artist"),
    path('track/<int:track_id>/', views.view_track, name="view_track"),
    path('dance/<int:dance_id>/', views.view_dance, name="view_dance"),
]