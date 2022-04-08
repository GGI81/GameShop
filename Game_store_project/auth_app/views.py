from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login
from Game_store_project.auth_app.forms import CreateProfileForm
# from Game_store_project.auth_app.common.custom_mixins import RedirectToDashboardMixin


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'auth_templates/registration.html'
    success_url = reverse_lazy('details')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

class UserLoginView(auth_views.LoginView):
    template_name = 'auth_templates/login.html'
    success_url = reverse_lazy('details')  # or can reverse_lazy('dashboard')


class UserLogoutView(auth_views.LogoutView):
    pass