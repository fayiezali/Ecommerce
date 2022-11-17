from django.urls import path
from . import views

# We are adding a URL called /dashboard & about
urlpatterns = [
    path('user-login'  , views.user_login, name='user-login-URL' ),
    path('user-logout' ,views.user_logout, name='user-logout-URL'),
]