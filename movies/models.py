from django.db import models

class Movie(models.Model):
    """
    Movie model representing film data with essential information
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    imgPath = models.CharField(max_length=255)
    duration = models.IntegerField()
    genre = models.CharField(max_length=255)  # Stored as comma-separated values
    language = models.CharField(max_length=100)
    mpaa_rating_type = models.CharField(max_length=10)
    mpaa_rating_label = models.CharField(max_length=100)
    user_rating = models.FloatField()
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
    
    def __str__(self):
        return self.name
    
    def get_genres(self):
        """Returns genre as a list instead of comma-separated string"""
        if isinstance(self.genre, str):
            return [g.strip() for g in self.genre.split(',')]
        return self.genre
