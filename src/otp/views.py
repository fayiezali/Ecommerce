from django.shortcuts import render , redirect
import random
from django.contrib.auth import login, authenticate ,logout
from django.contrib import messages
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from . models import otpMODEL 
from whatsapp.models import  SendOtpToWhatsappMODEL

from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes 
from project import settings
import datetime
# Send Whatsapp
import time
import webbrowser 
import pyautogui 
# Send OTP
import random
#
#
#
# Display Authorization Web Page
def display_authorization_DEF(request):
    return render(request,'otp/authorization.html', {})
#
# 
# Login With OTP Send one password To Email and whtsapp
def authorization_with_otp_DEF(request): # 
    # Verify that the data is protected
    if request.method == 'POST':
        # Receive user data
        username = request.POST['username']
        password = request.POST['password']
        # Check the username and password
        user = authenticate(request, username = username, password = password)
        # In the event that a user is found
        if user:
                # If the user account is active
                if user.is_active:
                    # Entry to the system
                    login(request, user)
                    # Definition of variables
                    date_time = ''
                    otp=''
                    # Save Current Date in variable
                    date_time = str(datetime.datetime.now())
                    # Save Current Random Number in variable
                    otp= f'{str(random.randint(1000,9999))}'
                    table_otp = otpMODEL.objects.get(otp_user=user.id)
                    table_otp.otp_one_time_password = otp
                    # Save the current otp in database
                    table_otp.save()
                    # messages when account has been created in database
                    messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
                    ########################################################################
                    # Send Message To Whatsapp - START
                    user_mobile_number = SendOtpToWhatsappMODEL.objects.get(SOTW_user=user.id)
                    # Verify that the WhatsApp service is active
                    # None:The Field Does Not Have Data - None = False
                    if user_mobile_number.SOTW_mobile_number is not None and user_mobile_number.Is_whatsApp_active == True:
                        message = "\n" + "One Time Password" + "\n" + "       " + "                                 Code: " +  otp + "       " + "\n" + "                               Date: "  + date_time + "            " +"Passing the verification code for others exposes your account to the risk of fraud"        
                        # Message='User Account Created - We Thank You and welcome you to join us.'   
                        webbrowser.open('https://web.whatsapp.com/send?phone='+ str(user_mobile_number.SOTW_mobile_number) +'&text='+message)
                        time.sleep(10) # Seconds of stillness
                        pyautogui.press('enter') # Click on Inter key
                        # Send Message To Whatsapp - END
                    ########################################################################
                        
                    #
                    # Send otp To Email - START
                    subject = "Welcome To Ecommerce Login!!"
                    # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to our Space!! \nThank you for visiting our website.\n We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n$p@r$h\nCEO of nothing"        
                    # message = "Hello " + user.first_name + "\n" + "One Time Password" + "\n" + "Code:  " +  otp +  "\n" + "Date/Time:  "  + str(datetime.datetime.now()) + "\n\nThanking You\nُemail@name.com\nThe Company's Name"        
                    message = "Hello " + user.first_name + "\n" + "One Time Password" + "\n" + "Code:  " +  otp +  "\n" + "Date:  "  + date_time + "\n" +"Passing the verification code for others exposes your account to the risk of fraud" + "\n\nThanking You\nُemail@name.com\nThe Company's Name"        
                    # the email we will be using to send it to teh the new user
                    from_email = settings.EMAIL_HOST_USER
                    # the user email
                    to_list = [user.email]
                    # fail_silently is used for the purpose that if teh email is not send, teh app should not crash 
                    send_mail(subject, message, from_email, to_list, fail_silently=True)
                    # Send otp To Email - END
                    messages.success(request,('User Is Active'))
                    messages.success(request,('otp_MODEL.save()'))
                    return redirect('display_authorization-URL')
                else:
                    messages.success(request,('User Is Not Active'))
                    return redirect('login_page-URL')
        else:
            messages.success(request,('User Name or Password Is Incorrect'))
            return redirect('login_page-URL')
    else:
        return redirect('login_page-URL')
#
#
# Resend OTP To Email and Whtsapp
def resend_otp_DEF(request): # 
    # Save the current user
    user = request.user
    # Definition of variables
    date_time = ''
    otp=''
    # Save Current Date in variable
    date_time = str(datetime.datetime.now())
    # Save Current Random Number in variable
    otp= f'{str(random.randint(1000,9999))}'
    # Save the current otp in var
    table_otp = otpMODEL.objects.get(otp_user=user.id)
    table_otp.otp_one_time_password = otp
    # Save the current otp in database
    table_otp.save()
    # messages when account has been created in database
    messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
    ########################################################################
    # Send Message To Whatsapp - START
    user_mobile_number = SendOtpToWhatsappMODEL.objects.get(SOTW_user=user.id)
    # Verify that the WhatsApp service is active
    if user_mobile_number.SOTW_mobile_number is not None and user_mobile_number.Is_whatsApp_active == True:
        message = "\n" + "One Time Password" + "\n" + "       " + "                                 Code: " +  otp + "       " + "\n" + "                               Date: "  + date_time + "            " +"Passing the verification code for others exposes your account to the risk of fraud"        
        # Message='User Account Created - We Thank You and welcome you to join us.'   
        webbrowser.open('https://web.whatsapp.com/send?phone='+ str(user_mobile_number.SOTW_mobile_number) +'&text='+message)
        time.sleep(10) # Seconds of stillness
        pyautogui.press('enter') # Click on Inter key
        # Send Message To Whatsapp - END
    ########################################################################
    # Send otp To Email - START
    subject = "Welcome To Ecommerce Login!!"
    # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to our Space!! \nThank you for visiting our website.\n We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n$p@r$h\nCEO of nothing"        
    # message = "Hello " + user.first_name + "\n" + "One Time Password" + "\n" + "Code:  " +  otp +  "\n" + "Date/Time:  "  + str(datetime.datetime.now()) + "\n\nThanking You\nُemail@name.com\nThe Company's Name"        
    message = "Hello " + user.first_name + "\n" + "One Time Password" + "\n" + "Code:  " +  otp +  "\n" + "Date:  "  + date_time + "\n" +"Passing the verification code for others exposes your account to the risk of fraud" + "\n\nThanking You\nُemail@name.com\nThe Company's Name"        
    # the email we will be using to send it to teh the new user
    from_email = settings.EMAIL_HOST_USER
    # the user email
    to_list = [user.email]
    # fail_silently is used for the purpose that if teh email is not send, teh app should not crash 
    send_mail(subject, message, from_email, to_list, fail_silently=True)
    # Send otp To Email - END
    return redirect('display_authorization-URL')




# Check the password for one time
def login_with_otp_DEF(request): # 
    if request.method == 'POST':
    # Verify that the name is not used by another user
        one_time_password_current= request.POST['txt_one_time_password_current']

        # Verify the number of input letters
        if len(one_time_password_current) != 4:
            messages.error(request, "The One Time Password is Incorrect!")
            return redirect('display_authorization-URL')
        if not one_time_password_current.isnumeric():
            messages.error(request, "The Password Must Be One Time Numbers")
            return redirect('display_authorization-URL')
        
        # Check the passwords match
        # If  One Time Password Exists In Database
        if otpMODEL.objects.filter(otp_one_time_password=one_time_password_current).exists():
            messages.success(request,('Youre logged in'))
            return redirect('dashboard-URL')
        else:
            logout(request)
            messages.success(request,('The One Time Password is Incorrect'))
            return redirect('login_page-URL')
    else:
        messages.success(request,('No POST method'))
        return redirect('login_page-URL')


