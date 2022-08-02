from django.views import generic

from .models import Contract


class IndexView(generic.ListView):
    model = Contract
    template_name = 'contracts/index.html'
    context_object_name = 'contracts'


class DetailView(generic.DetailView):
    model = Contract
    template_name = 'contracts/detail.html'
