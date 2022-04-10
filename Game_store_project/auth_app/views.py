from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import views as auth_views, login
from Game_store_project.auth_app.forms import CreateProfileForm
# from Game_store_project.auth_app.common.custom_mixins import RedirectToDashboardMixin
from Game_store_project.auth_app.models import UserProfile


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'auth_templates/registration.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

class UserLoginView(auth_views.LoginView):
    template_name = 'auth_templates/login.html'
    success_url = reverse_lazy('dashboard')  # or can reverse_lazy('details')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView, auth_mixins.LoginRequiredMixin):
    model = UserProfile
    template_name = 'auth_templates/profile_details.html'