from django.urls import path
from Game_store_project.game_store.views import IndexView, DashboardView, AddGameView, NoPermissionTemplate, \
    game_details_view, edit_game_view, delete_game_view

urlpatterns = (
    path('accounts/', IndexView.as_view(), name='index'),
    path('', DashboardView.as_view(), name='dashboard'),

    path('no-permissions/', NoPermissionTemplate.as_view(), name='no permissions'),

    path('game/add/', AddGameView.as_view(), name='add game'),
    path('game/edit/<int:pk>', edit_game_view, name='edit game'),
    path('game/delete/<int:pk>', delete_game_view, name='delete game'),
    path('game/description/<int:pk>', game_details_view, name='game details'),
)
