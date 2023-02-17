from django.urls import path
from . import views

urlpatterns = [
    # display the Page Generate Random Strong Password
    path('display_generate_random_strong_password/'         , views.display_generate_random_strong_password_DEF      , name='display_generate_random_strong_password-URL'),
#
    # Generate random password
    path('generate_random_strong_password/'                , views.generate_random_strong_password_DEF             , name='generate_random_strong_password-URL'),
#
    # Display the Page Send New Password To User
    path('display_send_new_password_to_user/'               , views.display_send_new_password_to_user_DEF             , name='display_send_new_password_to_user-URL'),
#
    # Function - Calling - With Not Return (Statement / Value) -  What The Job Is Doing: Send The New Password To User Email
    path('FUNCTION_send_new_password_to_user_email/'       , views.FUNCTION_send_new_password_to_user_email         , name='FUNCTION_send_new_password_to_user_email-URL'),
#
# Function - Defined - With Not Return (Statement / Value) - What The Job Is Doing: Send The New Password To User WhatsApp
    path('FUNCTION_send_new_password_to_user_email/'       , views.FUNCTION_send_new_password_to_user_whatsapp      , name='FUNCTION_send_new_password_to_user_whatsapp-URL'),
    #
] 

