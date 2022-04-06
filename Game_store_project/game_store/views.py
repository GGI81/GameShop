from django.shortcuts import render
from django.views import generic as views



class IndexView(views.TemplateView):
    template_name = 'game_store_templates/index.html'


class DetailsView(views.TemplateView):
    template_name = 'game_store_templates/profile_details.html'
