from management.commands.data_get import get_content
from django.shortcuts import redirect
from django.shortcuts import render
from models import Character
from models import Content
from models import Person
from models import Genre
from forms import AddContent


def add_content(request):
    if request.method == 'POST':
        form = AddContent(request.POST)
        if form.is_valid():
            imdb_url = form.cleaned_data['link']
            imdb_id = [imdb_url[26:35]]
            print get_content(imdb_id)
            return redirect("/movies")
    else:
        form = AddContent()
    return render(request, 'form.html', {'form': form})

def movies(request):
    movies = Content.objects.filter(type='movie').order_by('title', 'release_date')
    imdb_url = 'http://www.imdb.com/title/'
    args = {'movies': movies, 'include': 'includes/movie/movie.html', 'imdb_url': imdb_url}
    return render(request, "index.html", args)

def view_movie(request, movie_id):
    movies = Content.objects.filter(id=movie_id)
    characters = Character.objects.filter(content__id=movie_id).order_by('tomato_id')
    actors = Person.objects.filter(roles__content__id=movie_id).order_by('tomato_id')
    genres = Genre.objects.filter(content__id=movie_id).order_by('name')
    args = {'movies': movies, 'genres': genres,'actors': actors, 'characters': characters, 'include': 'includes/movie/view_movie.html'}
    return render(request, "index.html", args)

def series(request):
    series = Content.objects.filter(type='series').order_by('title', 'release_date')
    args = {'series': series, 'include': 'includes/series/series.html'}
    return render(request, "index.html", args)

def view_series(request, series_id):
    series = Content.objects.filter(id=series_id)
    characters = Character.objects.filter(content__id=series_id).order_by('tomato_id')
    actors = Person.objects.filter(roles__content__id=series_id).order_by('tomato_id')
    genres = Genre.objects.filter(content__id=series_id).order_by('name')
    args = {'series': series, 'genres': genres,'actors': actors, 'characters': characters, 'include': 'includes/series/view_series.html'}
    return render(request, "index.html", args)

def actors(request):
    actors = Person.objects.filter(type='actor').order_by('name')
    args = {'actors': actors, 'include': 'includes/actor/actor.html'}
    return render(request, "index.html", args)

def view_actor(request, series_id):
    actors = Person.objects.filter(id=actor_id)
    characters = Character.objects.filter(person__id=actor_id)
    series = Content.objects.filter(person__id=actor_id)
    args = {'series': series, 'genres': genres,'actors': actors, 'characters': characters, 'include': 'includes/series/view_series.html'}
    return render(request, "index.html", args)

def directors(request):
    directors = Person.objects.filter(type='director').order_by('name')
    args = {'directors': directors, 'include': 'includes/director/director.html'}
    return render(request, "index.html", args)

def writers(request):
    writers = Person.objects.filter(type='director').order_by('name')
    args = {'writers': writers, 'include': 'includes/writer/writer.html'}
    return render(request, "index.html", args)

def genres(request):
    genres = Genre.objects.all().order_by('name')
    args = {'genres': genres, 'include': 'includes/genre/genre.html'}
    return render(request, "index.html", args)

def view_genre(request, genre_id):
    genres = Genre.objects.filter(id=genre_id)
    content = Content.objects.filter(genre__id=genre_id).order_by('title')
    args = {'genres': genres, 'content': content, 'include': 'includes/genre/view_genre.html'}
    return render(request, "index.html", args)
