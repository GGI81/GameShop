from django.urls import path
from Game_store_project.game_store.views import IndexView, DashboardView, AddGameView, NoPermissionTemplate

urlpatterns = (
    path('accounts/', IndexView.as_view(), name='index'),
    path('', DashboardView.as_view(), name='dashboard'),

    path('no-permissions/', NoPermissionTemplate.as_view(), name='no permissions'),

    path('add/game/', AddGameView.as_view(), name='add game'),
)
