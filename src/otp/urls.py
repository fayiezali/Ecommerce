from django.urls import path
from otp import views
from django.urls import path
from . import views # This Views I Created It
#
#
# # AUTHENTICATION:-------------------------------------------------------------------------------------------------------
urlpatterns = [
        # Login In System
        # Verify using or TP before entering the system
        path('authorization_with_otp/'    , views.authorization_with_otp_DEF  ,  name='authorization_with_otp-URL' ),
        # Login With OTP
        path('login_with_otp/'          , views.login_with_otp_DEF         ,  name='login_with_otp-URL' ),
        # Resend OTP
        path('resend_otp/'             , views.resend_otp_DEF           ,  name='resend_otp_-URL' ),
        # Display the verification  page HTML using or otp
        path('authorization/'           , views.display_authorization_DEF   , name='display_authorization-URL')
] 
