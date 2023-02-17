from django.shortcuts import redirect, render
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from . models import SendOtpToWhatsappMODEL
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import re
import datetime
# Send Whatsapp
import time
# validation formula
MOBIL_NUMBER_REGEX  = re.compile(r"[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")
#
#
# # The Condition For Seeing The Required Page Login
# @login_required(login_url="login/")
# View the about Page
@login_required(login_url='login/')
# Display Authorization Web Page
def display_activate_whatsapp_service_DEF(request):
    return render(request,'whatsapp/activate_whatsApp_service.html', {})
#
#
#
def active_cancel_whatsapp_service_DEF(request):
    # Verify that the data is protected
    if request.method == 'POST':
        # Receive user data
        # # Save the current Mobile Number in var
        mobile_number_insert_by_user        = request.POST.get('mobile_number_for_active_or_cancel')
        filte_data_mobile_number_from_model  = SendOtpToWhatsappMODEL.objects.filter(SOTW_mobile_number=mobile_number_insert_by_user)
        # Save the current user
        user = request.user
        # Save the current Mobile Number in var
        table_mobile_number = SendOtpToWhatsappMODEL.objects.get(SOTW_user=user.id)

# defining some parameter for user to follow while making account
        #
        # Verify the validity of the inputs - UserName
        if not MOBIL_NUMBER_REGEX.match(str(mobile_number_insert_by_user)):
            messages.error(request, "Mobily Number - must be entered in the format: '+966000000000'.")
            return redirect('display_activate_whatsapp_service-URL')

        # Verify the number of input letters
        if len(mobile_number_insert_by_user)!=13:
            messages.error(request, "Mobily Number must be Equal 13 Numbers")
            return redirect('display_activate_whatsapp_service-URL')

        # Verify the number of input letters
        if  len(filte_data_mobile_number_from_model) ==0:
        # Activating WhatsApp
            # Save new data in field
            table_mobile_number.SOTW_mobile_number     = mobile_number_insert_by_user
            table_mobile_number.SOTW_Is_whatsApp_active  =True
            # Send messages To User
            messages.success(request, "Your WhatsApp Service has been Activated succesfully.")
        else:
        # Cancel WhatsApp activation
            # Save new data in field
            table_mobile_number.SOTW_mobile_number     = None
            table_mobile_number.SOTW_Is_whatsApp_active  =False
            # Send messages To User
            messages.success(request, "Your WhatsApp Service has been unactivated succesfully.")
    # Save the current Data in database
    table_mobile_number.save()
    return redirect('display_activate_whatsapp_service-URL')


