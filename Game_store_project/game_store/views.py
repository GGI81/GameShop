from django.shortcuts import render
from django.views import generic as views
from django.views.generic import DetailView

from Game_store_project.game_store.models import Games


class IndexView(views.TemplateView):
    template_name = 'game_store_templates/index.html'


class DashboardView(views.ListView):
    model = Games
    template_name = 'game_store_templates/dashboard.html'
    context_object_name = 'games'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     # context = super().get_context_data(**kwargs)
    #     # context['details'] = DetailView
    #     pass


class GameDetails(views.DetailView):
    model = Games