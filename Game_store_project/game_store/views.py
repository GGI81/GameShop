# from django.views import generic as views
# from django.shortcuts import redirect, render
# from django.contrib.auth import mixins as auth_mixins
# from Game_store_project.game_store.models import Games
#
#
#
# class IndexView(views.View):
#     @staticmethod
#     def get(request):
#         if request.user.is_authenticated:
#             return redirect('dashboard')
#         else:
#             return render(request, 'game_store_templates/index.html')
#
#
#
# class DashboardView(views.ListView, auth_mixins.LoginRequiredMixin):
#     model = Games
#     template_name = 'game_store_templates/dashboard.html'
#     context_object_name = 'games'
#
#
# # TODO have to make permissions and the admin will be able to add edit and delete games
#
#
#
