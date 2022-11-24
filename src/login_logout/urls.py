from django.urls import path
from . import views # This Views I Created It
from django.contrib.auth import views as auth_views # This Views Built-in Django
#
#
#
# AUTHENTICATION:-------------------------------------------------------------------------------------------------------
# Login - Logout - Logout Confirm - Logout Done (1) Login (1)
urlpatterns = [
        # Login In System
        # This Was Created By django
        path('login/',
        auth_views.LoginView.as_view(
        # The Name Of a Template To Display For The View Use
        template_name='login_logout/login.html',
        ),
        name='login-URL'),
        #
        #
        # Exit From System
        # thies Was Created By Django
        path('logout/',
        auth_views.LogoutView.as_view(
        # The Name Of a Template To Display For The View Use
        template_name='login_logout/logout_confirm.html', 
        ), 
        name='logout-URL'),
        #
        #
        # Logout Confirme
        # This is me created by me
        path('logout-confirm/',
        views.LogoutConfirmClass.as_view(
        template_name='login_logout/logout_confirm.html', # The Name Of a Template To Display For The View Use
        ),
        name='LogoutConfirm-URL'),
        #
        #
        # Checkout Confirmed Successfull
        # This is me created by me
        path('logout-done/',
        views.LogoutDoneClass.as_view(
        template_name='login_logout/logout_done.html'
        ),
        name='LogoutDone-URL'),
]
#