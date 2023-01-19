from django.urls import path
from . import views



# # AUTHENTICATION:-------------------------------------------------------------------------------------------------------
urlpatterns = [
        # View Whatsapp Activation Page
        path('display_activate_whatsapp/'          , views.display_activate_whatsapp_service_DEF   , name='display_activate_whatsapp_service-URL'),
        path('active_unactive_whatsapp_service/'   , views.active_cancel_whatsapp_service_DEF   , name='active_cancel_whatsapp_service-URL'),
] 
