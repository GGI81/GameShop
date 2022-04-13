# from django.urls import path
# from django.contrib.auth import views as auth_views
# from Game_store_project.auth_app.views import UserRegisterView, UserLoginView, UserLogoutView, ProfileDetailsView, \
#     EditProfileView, add_funds_view
#
# urlpatterns = (
#     path('registration/', UserRegisterView.as_view(), name='user registration'),
#     path('login/', UserLoginView.as_view(), name='user login'),
#     path('logout/', UserLogoutView.as_view(), name='user logout'),
#
#     path('profile-details/<int:pk>/', ProfileDetailsView.as_view(), name='details'),
#     path('profile/edit/<int:pk>', EditProfileView.as_view(), name='edit profile'),
#     path('profile/add-funds/<int:pk>', add_funds_view, name='add funds'),
#
#     path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
#     path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset-done'),
#     path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# )
#
# # 1 - Submit email form                                 // PasswordResetView.as_view()
# # 2 - Email sent success message                        // PasswordResetDoneView.as_view()
# # 3 - Link to password Rest form in email               // PasswordResetConfirmView.as_view()
# # 4 - Password successfully changed message             // PasswordResetCompleteView.as_view()
