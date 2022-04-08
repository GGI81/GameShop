from django.contrib import admin
from Game_store_project.game_store.models import Games


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    pass