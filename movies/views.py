from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def search_movies(request):
    query = request.GET.get('query', '')
    movies = Movie.objects.filter(name__icontains=query)
    
    results = []
    for movie in movies:
        results.append({
            'id': movie.id,
            'name': movie.name,
            'imgPath': movie.imgPath,
            'duration': movie.duration,
            'genre': movie.get_genres(),  # Use get_genres() to return a list
            'language': movie.language,
            'mpaa_rating_type': movie.mpaa_rating_type,
            'user_rating': movie.user_rating
        })
    
    return JsonResponse({'results': results})
