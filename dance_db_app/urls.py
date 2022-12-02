from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('artist/<int:artist_id>/', views.view_artist, name="view_artist"),
    path('track/<int:track_id>/', views.view_track, name="view_track"),
    path('dance/<int:dance_id>/', views.view_dance, name="view_dance"),

    path('artist/add/', views.view_add_artist, name="view_add_artist"),
    path('track/add/', views.view_add_track, name="view_add_track"),
    path('dance/add/', views.view_add_dance, name="view_add_dance"),

    path('artists/', views.view_artists, name="view_all_artists"),
    path('tracks/', views.view_tracks, name="view_all_tracks"),
    path('dances/', views.view_dances, name="view_all_dances"),
]