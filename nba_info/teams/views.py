from django.http import Http404, HttpResponse
from django.views import generic

from .models import Team


class IndexView(generic.ListView):
    model = Team
    template_name = 'teams/index.html'
    context_object_name = 'teams'

    def get_queryset(self):
        print('test')
        results = Team.objects.all()
        print(results)
        return results


class DetailView(generic.DetailView):
    model = Team
    template_name = 'teams/detail.html'
