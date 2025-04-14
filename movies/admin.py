from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'language', 'mpaa_rating_type', 'user_rating')
    list_filter = ('language', 'mpaa_rating_type')
    search_fields = ('name', 'description')
