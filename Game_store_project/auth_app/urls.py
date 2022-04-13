from django.urls import path
from django.contrib.auth import views as auth_views
from Game_store_project.auth_app.views import UserRegisterView, UserLoginView, UserLogoutView, ProfileDetailsView, \
    EditProfileView, add_funds_view, ChangePasswordView

urlpatterns = (
    path('registration/', UserRegisterView.as_view(), name='user registration'),
    path('login/', UserLoginView.as_view(), name='user login'),
    path('logout/', UserLogoutView.as_view(), name='user logout'),

    path('profile-details/<int:pk>/', ProfileDetailsView.as_view(), name='details'),
    path('profile/edit/<int:pk>', EditProfileView.as_view(), name='edit profile'),
    path('profile/add-funds/<int:pk>', add_funds_view, name='add funds'),
    path('profile/change-password/', ChangePasswordView.as_view(), name='change password')

    # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
)

# 1 - Submit email form                                 // PasswordResetView.as_view()
# 2 - Email sent success message                        // PasswordResetDoneView.as_view()
# 3 - Link to password Rest form in email               // PasswordResetConfirmView.as_view()
# 4 - Password successfully changed message             // PasswordResetCompleteView.as_view()
