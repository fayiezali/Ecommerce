from django.shortcuts import render , redirect
from django.contrib import messages



# Display ................
def messages_alert_DEF(request):
    messages.debug(  request, "Debug - Send message Testing")    
    messages.info(    request, "Info - Send message Testing")
    messages.success( request, "Success - Send message Testing")
    messages.warning(request, "Warning - Send message Testing")
    messages.error(  request, "Error - Send message Testing")
    return render(request, 'messages_alert/messages_alert.html', {})
