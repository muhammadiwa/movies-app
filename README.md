# Django Movie App

A web-based movie application built with Django that displays movie information and allows users to search for movies by name.

## Features

- Movie listing page with all movies
- Detailed movie information page
- Real-time search functionality using JavaScript
- Responsive design for mobile and desktop devices
- Movie data import from JSON file
- Automatic fetching of movie posters from TMDb API

## Project Structure

```
django-movie-app/
│
├── movie_app/              # Main project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI configuration
│
├── movies/                 # Movies application
│   ├── models.py           # Movie data model
│   ├── views.py            # View functions
│   ├── urls.py             # URL patterns for movies app
│   ├── admin.py            # Admin interface configuration
│   ├── migrations/         # Database migrations
│   └── management/         # Custom management commands
│       └── commands/
│           └── import_movies.py  # Command to import movies from JSON
│
├── templates/              # HTML templates
│   ├── base.html           # Base template with common structure
│   └── movies/
│       ├── movie_list.html # Template for movie listing
│       └── movie_detail.html # Template for movie details
│
├── static/                 # Static files
│   ├── css/
│   │   └── styles.css      # CSS styles
│   └── js/
│       └── search.js       # JavaScript for search functionality
│
├── movies.json             # Sample movie data in JSON format
├── requirements.txt        # Python dependencies
└── manage.py               # Django command-line utility
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd django-movie-app
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations to create the database:
   ```
   python3 manage.py makemigrations movies
   python3 manage.py migrate
   ```

5. Import movie data from the provided JSON file:
   ```
   python3 manage.py import_movies movies.json
   ```

6. Run the development server:
   ```
   python3 manage.py runserver
   ```

7. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## Usage

- The home page displays a list of all movies.
- Use the search bar to filter movies by name (searching happens in real-time).
- Click on any movie to view its detailed information.
- Navigate back to the movie list using the link at the bottom of the detail page or the header link.

## TMDb API Integration

This project uses the TMDb API to fetch movie posters. To enable this feature:
1. Sign up for a free account at [TMDb](https://www.themoviedb.org/).
2. Generate an API key from the [API section](https://www.themoviedb.org/settings/api).
3. Replace the placeholder `TMDB_API_KEY` in the `import_movies.py` file with your API key.

## Technologies Used

- **Backend**: Django 4.x, Python 3.x
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default)
- **Other**: TMDb API for fetching movie posters

## Development

To create a superuser for admin access:
```
python manage.py createsuperuser
```

Access the admin interface at:
```
http://127.0.0.1:8000/admin/
```

## Dependencies

All required Python packages are listed in `requirements.txt`. Install them using:
```
pip install -r requirements.txt
```
