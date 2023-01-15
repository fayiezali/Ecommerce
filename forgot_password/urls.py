from django.urls import path
from . import views

urlpatterns = [
    #
    path('generate_random_strong_password/'        , views.generate_random_strong_password_DEF        , name='generate_random_strong_password-URL'),
    #
    path('display_generate_random_strong_password/'  , views.display_generate_random_strong_password_DEF , name='display_generate_random_strong_password-URL'),
    #
] 


