from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import redirect, render
from django.contrib.auth import mixins as auth_mixins
from Game_store_project.game_store.models import Games
from django.contrib.auth.decorators import login_required
from Game_store_project.auth_app.models import UserProfile
from Game_store_project.game_store.forms import CreatingGameForm, EditGameForm, DeleteGameForm, GiveFeedbackForm, \
    AskAdmin


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.get(pk=self.request.user.id)
        return context


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


@login_required()
def game_details_view(request, pk):
    game = Games.objects.get(pk=pk)

    context = {
        'game': game,
    }

    return render(request, 'game_store_templates/game_description.html', context)


@login_required()
def edit_game_view(request, pk):
    game = Games.objects.get(pk=pk)
    if request.method == "POST":
        form = EditGameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditGameForm(instance=game)

    context = {
        'game': game,
        'form': form,
    }

    return render(request, 'game_store_templates/edit_game.html', context)


@login_required()
def delete_game_view(request, pk):
    game = Games.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteGameForm(request.POST, instance=game)

    context = {
        'game': game,
        'form': form,
    }

    return render(request, 'game_store_templates/delete_game.html', context)


@login_required()
def buy_game_view(request, pk):
    game = Games.objects.get(pk=pk)
    profile = UserProfile.objects.get(pk=request.user.id)

    buy_game = 'Buy'

    if request.GET.get('Buy Game') == buy_game:
        if profile.wallet >= game.price:
            profile.wallet -= game.price
            profile.games.add(game)
            profile.save()
            return redirect('dashboard')

        else:
            return redirect('not enough funds')

    context = {
        'game': game,
        'profile': profile,
    }

    return render(request, 'game_store_templates/buy_current_game.html', context)


class NotEnoughFunds(views.TemplateView, auth_mixins.LoginRequiredMixin):
    template_name = 'game_store_templates/not_enough_funds.html'


@login_required()
def owned_games_view(request):
    profile = UserProfile.objects.get(pk=request.user.id)

    games = profile.games.all()

    context = {
        'games': games,
        'profile': profile
    }

    return render(request, 'game_store_templates/bought_games.html', context)


class FeedbackView(views.View, auth_mixins.LoginRequiredMixin):
    @staticmethod
    def get(request):
        form = GiveFeedbackForm
        context = {
            'form': form,
        }

        return render(request, 'game_store_templates/feedback.html', context)


class NoPermissionTemplate(views.TemplateView):
    template_name = 'game_store_templates/template_for_no_permission.html'



def admin_ask_view(request):
    if request.method == "POST":
        form = AskAdmin(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AskAdmin(request.POST)

    context = {
        'form': form,
    }

    return render(request, 'game_store_templates/adminstext.html', context)
