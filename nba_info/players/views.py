from django.http import Http404, HttpResponse
from django.views import generic

from .models import Player


class IndexView(generic.ListView):
    model = Player
    template_name = 'players/index.html'
    context_object_name = 'players'


class DetailView(generic.DetailView):
    model = Player
    template_name = 'players/detail.html'
