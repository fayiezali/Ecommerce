from django.urls import path
from django.contrib.auth import views as auth_views # This Views Built-in Django
from django.urls import reverse_lazy
#
from . import views
#
#
#
urlpatterns = [
        path('changepassword/', views.change_password_DEF, name="changepassword-URL"),
        # path('changepassword', views.change_password_DEF, name="changepassword_URL"),
        # path('change-password/<int:id>/',views.change_password_DEF,name='changepassword-URL'),
]