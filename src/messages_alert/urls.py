from django.urls import path
from . import views # This Views I Created It
#
#
# Messages Alert With Bootstrap:-------------------------------------------------------------------------------------------------------
urlpatterns = [
        # Display ..........
        path('messages_alert/'  , views.messages_alert_DEF  ,  name='messages_alert-URL' ),

] 