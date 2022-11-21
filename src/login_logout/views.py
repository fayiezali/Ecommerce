from django.shortcuts import render
from django.views.generic import TemplateView
#
#
# Create your views here.
# Logout Confirm From App
class LogoutConfirmClass(TemplateView):
    template_name = 'login_logout/logout_confirm.html' # The Page HTML to Display
#
# Logout Done From App
class LogoutDoneClass(TemplateView):
    template_name = 'login_logout/logout_done.html' # The Page HTML to Display
#
