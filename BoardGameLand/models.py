from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Genre(models.Model):
    """Model representing a game genre."""
    name = models.CharField(max_length=200, help_text='Enter a game genre (e.g. Strategy)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Game(models.Model):
    """Model representing a game."""
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the game')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def get_absolute_url(self):
        """Returns the url to access a detail record for this game."""
        return reverse('game', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class User(models.Model):
    """Model representing a user."""
    given_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=75)

    def __str__(self):
        """String for representing the Model object"""
        return self.surname + ", " + self.given_name

class Cart(models.Model):
    """Model representing a cart."""
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    items = models.ManyToManyField(Game, help_text="list of items in user's shopping cart.")

    def __str__(self):
        """String for representing the Model object"""
        return self.items
