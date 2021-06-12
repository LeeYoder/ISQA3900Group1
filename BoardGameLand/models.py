from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    """Model representing a game genre."""
    name = models.CharField(max_length=200, help_text='Enter a game genre (e.g. Strategy)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Game(models.Model):
    """Model representing a game."""
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the game')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        """String for representing the Model object."""
        return self.title
