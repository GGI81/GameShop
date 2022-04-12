from django.urls import path

from Game_store_project.auth_app.views import UserRegisterView, UserLoginView, UserLogoutView, ProfileDetailsView, \
    EditProfileView, add_funds_view

urlpatterns = (
    path('registration/', UserRegisterView.as_view(), name='user registration'),
    path('login/', UserLoginView.as_view(), name='user login'),
    path('logout/', UserLogoutView.as_view(), name='user logout'),

    path('profile-details/<int:pk>/', ProfileDetailsView.as_view(), name='details'),
    path('profile/edit/<int:pk>', EditProfileView.as_view(), name='edit profile'),
    path('profile/add-funds/<int:pk>', add_funds_view, name='add funds'),
)
