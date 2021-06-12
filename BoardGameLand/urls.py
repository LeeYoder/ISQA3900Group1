from . import views
from django.urls import path, re_path

app_name = 'BoardGameLand'
urlpatterns = [
    path('', views.home, name='home'),
]