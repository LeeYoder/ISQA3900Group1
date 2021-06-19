from django.shortcuts import render
from BoardGameLand.models import Game, Genre
from django.views import generic

# Create your views here.

def home(request):
    return render(request, 'homepage.html')

class GameList(generic.ListView):
    model = Game
    paginate_by = 9

class Game(generic.DetailView):
    model = Game
