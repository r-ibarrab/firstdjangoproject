from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    print(list(movies))
    return render(request,'movies/index.html',dict(movies=movies))

def detail(request, movie_id):
    print('\n\n AHHH ',movie_id,'\n\n')
    one_movie = Movie.objects.get(pk=movie_id)
    return render(request,'movies/detail.html',dict(movie=one_movie))

# Create your views here.
