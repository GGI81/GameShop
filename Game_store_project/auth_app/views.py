from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import redirect, render
from django.contrib.auth import mixins as auth_mixins
from Game_store_project.auth_app.models import UserProfile
from django.contrib.auth import views as auth_views, login
from Game_store_project.auth_app.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm


# from Game_store_project.auth_app.common.custom_mixins import RedirectToDashboardMixin


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


# TODO
# class ChangePassword(auth_views.PasswordChangeView):
#     pass


# FBV
def edit_profile_view(request, pk):
    profile = UserProfile.objects.get(pk=pk)
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'auth_templates/edit.html', context)



class ConfirmationForDeletingProfileView(views.DeleteView):
    model = UserProfile
    template_name = 'auth_templates/confirmation_for_delete.html'
    success_url = reverse_lazy('index')

