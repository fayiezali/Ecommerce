from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('register', views.register_DEF, name='register-URL'),
    # path('signin', views.signin, name='signin'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('signout', views.signout, name='signout'),
]
