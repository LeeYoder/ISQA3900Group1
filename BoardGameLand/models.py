from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.contrib.auth.models import User
from datetime import date


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
    price = models.TextField(max_length=5)

    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        """String for representing the Model object."""
        return self.title
