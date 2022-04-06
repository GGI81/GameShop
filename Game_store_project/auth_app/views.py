from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from Game_store_project.auth_app.forms import CreateProfileForm
# from Game_store_project.auth_app.common.custom_mixins import RedirectToDashboardMixin


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'auth_templates/registration.html'
    success_url = reverse_lazy('details')



class UserLoginView(auth_views.LoginView):
    pass


class UserLogoutView(auth_views.LogoutView):
    pass
