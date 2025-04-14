import json
import os
import requests
from django.core.management.base import BaseCommand, CommandError
from movies.models import Movie

TMDB_API_KEY = 'a61f3e9e157b2af3627cd3639a767ad5'  # Replace with your TMDb API key
TMDB_BASE_URL = 'https://api.themoviedb.org/3'

class Command(BaseCommand):
    help = 'Import or update movies from a JSON file and fetch poster images from TMDb'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def fetch_poster_url(self, movie_name):
        """Fetch the poster URL for a movie from TMDb."""
        try:
            response = requests.get(
                f'{TMDB_BASE_URL}/search/movie',
                params={'api_key': TMDB_API_KEY, 'query': movie_name}
            )
            response.raise_for_status()
            data = response.json()
            if data['results']:
                poster_path = data['results'][0].get('poster_path')
                if poster_path:
                    return f'https://image.tmdb.org/t/p/w500{poster_path}'
        except Exception as e:
            self.stderr.write(f"Error fetching poster for '{movie_name}': {e}")
        return None

    def handle(self, *args, **options):
        json_file = options['json_file']
        
        if not os.path.exists(json_file):
            raise CommandError(f'JSON file "{json_file}" does not exist')
        
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                movies_data = json.load(file)
            
            imported_count = 0
            updated_count = 0
            
            for movie_data in movies_data:
                # Convert genre list to a comma-separated string if necessary
                genre = movie_data['genre']
                if isinstance(genre, list):
                    genre = ', '.join(genre)
                
                # Fetch poster URL from TMDb
                poster_url = self.fetch_poster_url(movie_data['name'])
                if poster_url:
                    movie_data['imgPath'] = poster_url
                
                movie, created = Movie.objects.update_or_create(
                    id=movie_data['id'],  # This is the lookup key
                    defaults={
                        'name': movie_data['name'],
                        'description': movie_data['description'],
                        'imgPath': movie_data.get('imgPath', ''),  # Use fetched poster URL
                        'duration': movie_data['duration'],
                        'genre': genre,  # Save as a comma-separated string
                        'language': movie_data['language'],
                        'mpaa_rating_type': movie_data['mpaaRating']['type'],
                        'mpaa_rating_label': movie_data['mpaaRating']['label'],
                        'user_rating': movie_data['userRating']
                    }
                )
                
                if created:
                    imported_count += 1
                else:
                    updated_count += 1
            
            self.stdout.write(self.style.SUCCESS(
                f'Successfully imported {imported_count} and updated {updated_count} movies'
            ))
        except json.JSONDecodeError:
            raise CommandError(f'Invalid JSON format in "{json_file}"')
        except KeyError as e:
            raise CommandError(f'Missing required field in JSON data: {str(e)}')
        except Exception as e:
            raise CommandError(f'Error importing movies: {str(e)}')
