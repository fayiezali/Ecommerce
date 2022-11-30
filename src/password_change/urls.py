from django.urls import path
from django.contrib.auth import views as auth_views # This Views Built-in Django
from django.urls import reverse_lazy
#
#
#
# Change Password - Password Change Done
urlpatterns = [
        # thies Was Created By Django
        # Change Password
        path('change-password/',
        auth_views.PasswordChangeView.as_view(
        template_name='password_change/change-password.html', # The Name Of a Template To Display For The View Use
        success_url= reverse_lazy('password_change_done')), # Redirect To URL Address
        name='password_change'), # Name URL pattern
#
#
        # Password Change completed Succesfull
        # thies Was Created By Django
        path('password_change_done/',
        auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change/password-change-done.html'), # The Name Of a Template To Display For The View Use
        name='password_change_done'), # Name URL pattern
#
]