import json
import os
from django.db import migrations

def import_movies(apps, schema_editor):
    Movie = apps.get_model('movies', 'Movie')
    
    # Get the path to the JSON file
    json_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'movies.json')
    
    try:
        with open(json_file_path, 'r') as file:
            movies_data = json.load(file)
            
            for movie_data in movies_data:
                Movie.objects.create(
                    id=movie_data['id'],
                    name=movie_data['name'],
                    description=movie_data['description'],
                    imgPath=movie_data['imgPath'],
                    duration=movie_data['duration'],
                    genre=movie_data['genre'],
                    language=movie_data['language'],
                    mpaa_rating_type=movie_data['mpaaRating']['type'],
                    mpaa_rating_label=movie_data['mpaaRating']['label'],
                    user_rating=movie_data['userRating']
                )
    except FileNotFoundError:
        print(f"Warning: Could not find movies.json at {json_file_path}")
    except Exception as e:
        print(f"Error importing movies: {e}")

def reverse_import(apps, schema_editor):
    Movie = apps.get_model('movies', 'Movie')
    Movie.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_movies, reverse_import),
    ]
