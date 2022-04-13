from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import redirect, render
from django.contrib.auth import mixins as auth_mixins
from Game_store_project.game_store.models import Games
from Game_store_project.game_store.forms import CreatingGameForm


class IndexView(views.View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'game_store_templates/index.html')


class DashboardView(views.ListView, auth_mixins.LoginRequiredMixin):
    model = Games
    template_name = 'game_store_templates/dashboard.html'
    context_object_name = 'games'


# TODO have to make permissions and the admin will be able to add edit and delete games


class NoPermissionTemplate(views.TemplateView):
    template_name = 'game_store_templates/template_for_no_permission.html'


class AddGameView(views.CreateView, auth_mixins.LoginRequiredMixin, auth_mixins.PermissionRequiredMixin):
    template_name = 'game_store_templates/add_game.html'
    permission_required = 'game_store.add_games'
    success_url = reverse_lazy('dashboard')
    queryset = Games
    form_class = CreatingGameForm

    def has_permission(self):
        user = self.request.user
        if user.has_perm('game_store.add_games'):
            return redirect('add game')
        else:
            return redirect('no permissions')



class EditGameView(views.UpdateView, auth_mixins.LoginRequiredMixin, auth_mixins.PermissionRequiredMixin):
    pass


class DeleteGameView(views.UpdateView, auth_mixins.LoginRequiredMixin, auth_mixins.PermissionRequiredMixin):
    pass
