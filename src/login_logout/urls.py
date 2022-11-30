from django.urls import path
from django.contrib.auth import views as auth_views # This Views Built-in Django
from . import views # This Views I Created It
#
#
# AUTHENTICATION:-------------------------------------------------------------------------------------------------------
# This Was Created By django (1)
# Login - Logout 
urlpatterns = [
        # Login In System
        # The Name Of a Template To Display For The View Use
        path('login/',
        auth_views.LoginView.as_view(
        template_name='login_logout/login.html',),
        name='login'),
#
#
        # Exit From System
        # thies Was Created By Django
        # The Name Of a Template To Display For The View Use
        path('logout/',
        auth_views.LogoutView.as_view(
        template_name='login_logout/logout_confirm.html',), 
        name='logout'),
#
#
]
#
# This is me created by me (1)
# Logout Confirm - Logout Done  Login 
urlpatterns += [
        # Logout Confirme
        # The Name Of a Template To Display For The View Use
        path('logout-confirm/',
        views.LogoutConfirmClass.as_view(
        template_name='login_logout/logout_confirm.html',),
        name='LogoutConfirm-URL'),
#
#
        # Checkout Confirmed Successfull
        # This is me created by me
        path('logout-done/',
        views.LogoutDoneClass.as_view(
        template_name='login_logout/logout_done.html'),
        name='LogoutDone-URL'),
]
#

# urlpatterns += [
#         path('user-login'  , views.user_login, name='user-login-URL' ),
# ] 