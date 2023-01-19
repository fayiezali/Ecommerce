from django.urls import path
from . import views

urlpatterns = [
    #
    path('display_generate_random_strong_password/'  , views.display_generate_random_strong_password_DEF   , name='display_generate_random_strong_password-URL'),
    #
    path('generate_random_strong_password/'         , views.generate_random_strong_password_DEF         , name='generate_random_strong_password-URL'),
    #
    path('display_send_new_password_to_user/'        , views.display_send_new_password_to_user_DEF        , name='display_send_new_password_to_user-URL'),
    
    path('send_new_password_to_user_email/'         , views.send_new_password_to_user_email_DEF          , name='send_new_password_to_user_email-URL'),
    #
    path('send_new_password_to_user_whatsapp/'      , views.send_new_password_to_user_whatsapp_DEF       , name='send_new_password_to_user_whatsapp-URL'),

] 
