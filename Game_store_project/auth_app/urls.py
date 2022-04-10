from django.urls import path

from Game_store_project.auth_app.views import UserRegisterView, UserLoginView, UserLogoutView, ProfileDetailsView, \
    edit_profile_view, ConfirmationForDeletingProfileView

urlpatterns = (
    path('registration/', UserRegisterView.as_view(), name='user registration'),
    path('login/', UserLoginView.as_view(), name='user login'),
    path('logout/', UserLogoutView.as_view(), name='user logout'),

    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='details'),
    path('profile/edit/<int:pk>', edit_profile_view, name='edit profile'),
    path('profile/delete<int:pk>', ConfirmationForDeletingProfileView.as_view(), name='delete profile'),
)