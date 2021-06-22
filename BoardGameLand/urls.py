from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.GameList.as_view(), name='games'),
    path('game/<int:pk>', views.Game.as_view(), name='game'),
    path('user/<int:pk>/cart/', views.cart, name='cart')
]
