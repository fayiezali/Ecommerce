from django.urls import path
from . import views # This Views I Created It
#
#
# # AUTHENTICATION:-------------------------------------------------------------------------------------------------------
urlpatterns = [
        # Login In System
        # The Name Of a Template To Display For The View Use
        path('login/'          , views.login_DEF          ,  name='login-URL' ),
        # Display Login Web Page
        path('login_page/'     , views.login_page_DEF      ,  name='login_page-URL' ),
        # Logout Confirme
        path('logout_confirm/'  , views.logout_confirm_DEF  ,  name='logout_confirm-URL' ),
        # Checkout Confirmed Successfull
        path('logout_done/'    , views.logout_done_DEF     ,  name='logout_done-URL' ),
] 