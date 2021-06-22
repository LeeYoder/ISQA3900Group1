from django.contrib.auth.decorators import login_required
from django.shortcuts import render #, get_object_or_404
from BoardGameLand.models import *
#from django.db.models import Sum
from django.views import generic

# Create your views here.

def home(request):
    return render(request, 'homepage.html')

class GameList(generic.ListView):
    model = Game
    paginate_by = 9

class Game(generic.DetailView):
    model = Game

@login_required
def cart(request, pk):
    #user = get_object_or_404(User, pk=pk)
    items = Cart.objects.filter(user_id=pk)
    total_price = 0
    for item in items:
        total_price += item.price
    return render(request, 'BoardGameLand/cart.html', {#'user': user,
                                                       'items': items,
                                                       'total_price': total_price})
