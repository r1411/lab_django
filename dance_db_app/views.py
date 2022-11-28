from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Artist

# Create your views here.
def index(request):
    latest_artists_list = Artist.objects.order_by('-id')[:3]

    template = loader.get_template('dance_db_app/index.html')
    context = {
        'artists': latest_artists_list
    }
    return HttpResponse(template.render(context, request))

def view_artist(request, artist_id):
    return HttpResponse(f"You're looking at artist {artist_id}.")

def view_track(request, track_id):
    return HttpResponse(f"You're looking at track {track_id}.")

def view_dance(request, dance_id):
    return HttpResponse(f"You're looking at dance {dance_id}.")