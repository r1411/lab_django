from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Artist, Track, Dance

# Create your views here.
def index(request):
    latest_artists_list = Artist.objects.order_by('-id')[:3]
    latest_tracks_list = Track.objects.order_by('-id')[:3]
    latest_dances_list = Dance.objects.order_by('-id')[:3]

    template = loader.get_template('dance_db_app/index.html')
    context = {
        'artists': latest_artists_list,
        'tracks': latest_tracks_list,
        'dances': latest_dances_list,
    }
    return HttpResponse(template.render(context, request))

def view_artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'dance_db_app/artist.html', {'artist': artist})

def view_track(request, track_id):
    return HttpResponse(f"You're looking at track {track_id}.")

def view_dance(request, dance_id):
    return HttpResponse(f"You're looking at dance {dance_id}.")

def view_artists(request):
    template = loader.get_template('dance_db_app/artists.html')
    context = {
        'artists': Artist.objects.all()
    }
    return HttpResponse(template.render(context, request))

def view_tracks(request):
    template = loader.get_template('dance_db_app/tracks.html')
    context = {
        'tracks': Track.objects.all()
    }
    return HttpResponse(template.render(context, request))

def view_dances(request):
    template = loader.get_template('dance_db_app/dances.html')
    context = {
        'dances': Dance.objects.all()
    }
    return HttpResponse(template.render(context, request))