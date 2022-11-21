from django.urls import path
from . import views # This Views I Created It
from django.contrib.auth import views as auth_views # This Views Built-in Django
from django.urls import reverse_lazy
#
#
#

# Change Password - Password Change Done (2)
urlpatterns = [
        # thies Was Created By Django
        # Change Password
        path('change-password/'                         , auth_views.PasswordChangeView.as_view(
        template_name='registration/change-password.html', # The Name Of a Template To Display For The View Use
        success_url= reverse_lazy('password_change_done')), # Redirect To URL Address
        name='password_change'), # Name URL pattern
        #
        # Password Change completed Succesfull
        # thies Was Created By Django
        path('password_change_done/'                   , auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password-change-done.html'), # The Name Of a Template To Display For The View Use
        name='password_change_done'), # Name URL pattern
# Password Reset - Password Reset Done - Password Reset Confirm - Password Reset Comlete (3)
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        #The Full Name Of a Template To Use For GEnerating The Email With The Reset Password Link
        # The URL To Redirect To After a Successful Password Reset Request
        # thies Was Created By Django
        path('password-reset/'                         , auth_views.PasswordResetView.as_view(
        template_name='registration/password_resetHTML.html', # The Name Of a Template To Display For The View Use
        subject_template_name='registration/password_reset_subject.txt',
        success_url= reverse_lazy('password_reset_done')), # Redirect To URL Address
        name='password_reset'), # Name URL pattern
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        # thies Was Created By Django
        path('password-reset/done/'                    , auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_doneHTML.html'), # The Name Of a Template To Display For The View Use
        name='password_reset_done'), # Name URL pattern
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        # thies Was Created By Django
        path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirmHTML.html'), # The Name Of a Template To Display For The View Use
        name='password_reset_confirm'), # Name URL pattern
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        # thies Was Created By Django
        path('password-reset-complete/'               , auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_completeHTML.html'), # The Name Of a Template To Display For The View Use
        name='password_reset_complete'), # Name URL pattern
]
#
#
# # AUTHENTICATION:-------------------------------------------------------------------------------------------------------
# # Login - Logout - Logout Confirm - Logout Done (1) Login (1)
# urlpatterns = [
#         # Login In System
#         # This Was Created By django
#         path('login/'                                   , auth_views.LoginView.as_view()         , name='login-URL'),
#         # Exit From System
#         # thies Was Created By Django
#         path('logout/'                                  , auth_views.LogoutView.as_view()        , name='logout-URL'),
#         # Logout Confirme
#         # This is me created by me
#         path('logout-confirm/'                          , views.LogoutConfirmClass.as_view()     , name='LogoutConfirm-URL'),
#         # Checkout Confirmed Successfull
#         # This is me created by me
#         path('logout-done/'                             , views.LogoutDoneClass.as_view()        , name='LogoutDone-URL'),
# ]
#
#
#


