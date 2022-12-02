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
    track = get_object_or_404(Track, pk=track_id)
    return render(request, 'dance_db_app/track.html', {'track': track})

def view_dance(request, dance_id):
    dance = get_object_or_404(Dance, pk=dance_id)
    return render(request, 'dance_db_app/dance.html', {'dance': dance})

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

def view_add_artist(request):
    template = loader.get_template('dance_db_app/add_artist.html')
    context = {

    }
    if all(['artist_name' in request.POST, 'artist_birthday' in request.POST, 'artist_country' in request.POST]):
        artist = Artist(name=request.POST['artist_name'], birthday=request.POST['artist_birthday'], country=request.POST['artist_country'])
        artist.save()
        context['msg'] = f'Артист {request.POST["artist_name"]} успешно добавлен!'
    return HttpResponse(template.render(context, request))

def view_add_track(request):
    template = loader.get_template('dance_db_app/add_track.html')
    context = {
        'artists': Artist.objects.all()
    }
    if all(['artist_id' in request.POST, 'track_title' in request.POST, 'track_duration' in request.POST]):
        track_artist = get_object_or_404(Artist, pk=request.POST['artist_id'])
        track = Track(title=request.POST['track_title'], duration=request.POST['track_duration'], artist=track_artist)
        track.save()
        context['msg'] = f'Трек {request.POST["track_title"]} успешно добавлен!'
    return HttpResponse(template.render(context, request))

def view_add_dance(request):
    template = loader.get_template('dance_db_app/add_dance.html')
    context = {
        'tracks': Track.objects.all()
    }
    if all(['track_id' in request.POST, 'dance_title' in request.POST, 'dance_difficulty' in request.POST]):
        dance_track = get_object_or_404(Track, pk=request.POST['track_id'])
        dance = Dance(title=request.POST['dance_title'], difficulty=request.POST['dance_difficulty'], track=dance_track)
        dance.save()
        context['msg'] = f'Танец {request.POST["dance_title"]} успешно добавлен!'
    return HttpResponse(template.render(context, request))