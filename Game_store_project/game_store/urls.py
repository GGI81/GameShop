from django.urls import path

from Game_store_project.game_store.views import IndexView, DashboardView, GameDetails

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('game/details/', GameDetails.as_view(), name='game details'),
)
