from django.http import Http404, HttpResponse
from django.template import loader
from .models import Player


def index(request):
    players = Player.objects.all()
    context = {
        'players': players
    }

    template = loader.get_template('players/index.html')
    return HttpResponse(template.render(context, request))


def detail(request, player_id):
    try:
        player = Player.objects.get(pk=player_id)
    except Player.DoesNotExist:
        raise Http404(f'Player {player_id} does not exist.')

    context = {
        'player': player
    }
    template = loader.get_template('players/detail.html')
    return HttpResponse(template.render(context, request))
