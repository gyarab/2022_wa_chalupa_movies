from django.shortcuts import render
from .models import Movie, Director, Actor, Genre, Comment
from .forms import CommentForm


def homepage(request):
    context = {"movies": Movie.objects.all()}
    return render(request, "homepage.html", context)


def directors(request):
    context = {"directors": Director.objects.all()}
    return render(request, "directors.html", context)


def director(request, id):
    context = {"director": Director.objects.get(id=id)}
    return render(request, "director.html", context)


def movies(request):
    context = {"movies": Movie.objects.all()}
    return render(request, "movies.html", context)


def movie(request, id):
    m = Movie.objects.get(id=id)
    f = CommentForm()

    if request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            c = Comment(
                movie=m,
                author=f.cleaned_data.get("author"),
                text=f.cleaned_data.get("text"),
                rating=f.cleaned_data.get("rating"),
            )
            if not c.author:
                c.author = "Anonym"
            c.save()
            f = CommentForm()

    context = {
        "movie": m,
        "comments": Comment.objects.filter(movie=m).order_by("-created_at"),
        "form": f,
    }
    return render(request, "movie.html", context)


def actors(request):
    context = {"actors": Actor.objects.all()}
    return render(request, "actors.html", context)


def actor(request, id):
    context = {"actor": Actor.objects.get(id=id)}
    return render(request, "actor.html", context)
