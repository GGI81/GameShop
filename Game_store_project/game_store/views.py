from django.urls import reverse_lazy
from django.views import generic as views
from Game_store_project.game_store.models import Games
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class IndexView(views.TemplateView):
    template_name = 'game_store_templates/index.html'


class DashboardView(views.ListView, LoginRequiredMixin):
    model = Games
    template_name = 'game_store_templates/dashboard.html'
    context_object_name = 'games'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     # context = super().get_context_data(**kwargs)
    #     # context['details'] = DetailView
    #     pass


class GameDetails(views.DetailView):
    model = Games


class AddNewGame(views.CreateView, PermissionRequiredMixin, LoginRequiredMixin):
    permission_required = 'game_store.change_games'
    model = Games
    success_url = reverse_lazy('dashboard')
    template_name = 'game_store_templates/add_game.html'
    fields = '__all__'
