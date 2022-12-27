from django.urls import path
from otp import views


from django.urls import path
from . import views # This Views I Created It
#
#
# # AUTHENTICATION:-------------------------------------------------------------------------------------------------------
urlpatterns = [
        # Login In System
        # The Name Of a Template To Display For The View Use
        path('authorization_with_otp/'   , views.authorization_with_otp_DEF   ,  name='authorization_with_otp-URL' ),
        path('login_with_otp/'          , views.login_with_otp_DEF         ,  name='login_with_otp-URL' ),
        # Display Login Web Page
        # path('login_page/'     , views.login_page_DEF              ,  name='login_page-URL' ),
] 
#
#
# # OTP :-------------------------------------------------------------------------------------------------------
# urlpatterns += [
#     path('number-random/', views.number_random_DEF, name='number_random-URL')
# ]
#
#
# # OTP :-------------------------------------------------------------------------------------------------------
urlpatterns += [
    path('authorization/', views.authorization_DEF, name='authorization-URL')
]