from django.views import generic

from .models import Team


class IndexView(generic.ListView):
    model = Team
    template_name = 'teams/index.html'
    context_object_name = 'teams'


class DetailView(generic.DetailView):
    model = Team
    template_name = 'teams/detail.html'
