from django.urls import path

from Game_store_project.game_store.views import IndexView, DetailsView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('', DetailsView.as_view(), name='details')
)