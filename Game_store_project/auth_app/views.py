from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from Game_store_project.auth_app.models import UserProfile
from django.contrib.auth import views as auth_views, login
from Game_store_project.auth_app.forms import CreateProfileForm, EditProfileForm


# CBV
class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts_templates/registration.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts_templates/login.html'
    success_url = reverse_lazy('dashboard')  # or can reverse_lazy('details')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    pass


class EditProfileView(views.UpdateView, auth_mixins.LoginRequiredMixin):
    model = UserProfile
    template_name = 'accounts_templates/edit.html'
    form_class = EditProfileForm

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.object.pk})


class ProfileDetailsView(views.DetailView, auth_mixins.LoginRequiredMixin):
    model = UserProfile
    template_name = 'accounts_templates/profile_details.html'


# Todo => have to correct code to be able to upload images after editing profile

# TODO
# class ChangePassword(auth_views.PasswordChangeView):
#     pass


# FBV
def add_funds_view(request, pk):
    profile = UserProfile.objects.get(pk=pk)

    five = 'Add 5$'
    ten = 'Add 10$'
    twenty = 'Add 20$'
    fifty = 'Add 50$'


    if request.GET.get('Five') == five:
        profile.wallet += 5
    elif request.GET.get('Ten') == ten:
        profile.wallet += 10
    elif request.GET.get('Twenty') == twenty:
        profile.wallet += 20
    elif request.GET.get('Fifty') == fifty:
        profile.wallet += 50

    profile.save()
    return render(request, 'accounts_templates/add_funds.html')
