from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.contrib.sites.shortcuts import get_current_site
from whatsapp.models import  SendOtpToWhatsappMODEL
from django.conf import settings
from django.core.mail import send_mail
# write a program to display the different random string method using the secrets.choice().  
# imports necessary packages  
import string  
import secrets  
import datetime
# Send Whatsapp
import time
import webbrowser 
import pyautogui 
# Send OTP
import random
import re
from django.contrib.auth.hashers import make_password, check_password
#
# validation formula
EMAIL_REGEX      = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
MOBIL_NUMBER_REGEX  = re.compile(r"[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")


'''
Python Modules:
## String Module
This module in Python is used to manipulate strings. It comes with a lot of functionalities that we can use in our Python code for strings.
1- string.ascii_letters(): This returns all the ASCII letters which are available.
2- string.ascii_uppercase(): This return all the ASCII letters in upper case.
3- string.ascii_lowercase(): This return all the ASCII letters in lower case.
4- string.octdigits(): This return all the octal digits.
5- string.hexdigits(): This return all the hexa digits.
6- string.digits(): This return all the digits.
7- string.punctuation(): This return all the special characters or punctuations.
7- string.capwords(): This makes the first character of each word in the capital title. It also takes a second parameter which can be used as a separator for capital letters. 
'''

# Display Web Page Generate Random Strog Password 
def display_generate_random_strong_password_DEF(request):
    return render(request,'forgot_password/generate_random_strong_password.html')


# Display Web Page Send Random Strong Password To User
def display_send_new_password_to_user_DEF(request):
    return render(request,'forgot_password/send_new_password_to_user.html')


# Function - Defined - With Return (Statement / Value) - What The Job Is Doing:Generate Random Strong Password 
def FUNCTION_generate_random_strong_password(): 
    length_password = 10 # define the length of the string 
    # Variable to save the password
    send_result_function_generate_random_strong_password = ''.join(secrets.choice
    (
    string.hexdigits    # This return all the hexa digits.
    # string.octdigits +   # This return all the octal digits.
    # string.ascii_letters   # String Digits Only
    ) 
    for x in range(length_password))  
    return send_result_function_generate_random_strong_password


# Function - Calling - With Return (Statement / Value) -  Generate Random Strong Password 
def  generate_random_strong_password_DEF(request):
    # Calling Function and Save Data in the variable  
    received_data = FUNCTION_generate_random_strong_password()    
    print('Function Calling: Received Data:' , received_data) 
    # Send The (context) to The Page HTML
    context = {'received_data': received_data}
    return render(request , 'forgot_password/generate_random_strong_password.html', context )


# Send The New Password To User Email
def FUNCTION_send_new_password_to_user_email(request): # 
    # Verify that the data is protected
    if request.method == 'POST':
        # Receive user data
        email_insert_by_user = request.POST['send_new_password_to_user_email']
        # Verify the validity of the inputs - Email
        if not EMAIL_REGEX.match(email_insert_by_user):
            messages.error(request, "EMAIL - The Entrance e-mail Is Not Registered With Us")
            return redirect('display_send_new_password_to_user-URL')

        # Verify that the Email is not used by another user
        if User.objects.filter(email=email_insert_by_user).exists():
            messages.error(request, "Email - Congratulations, Your Email Has Been Verified In Our Records")

            # Search the user with the desired e -mail
            user_set = User.objects.filter(email=email_insert_by_user)
            # Get the user's object in all its methods and attributes
            userObj = user_set[0] # Save the user in the variable

            current_user = userObj # Save the user in the variable        
            # In the event that a user is found
            if current_user:
                    # If the user account is active
                    if current_user.is_active:
                        # Definition of variables
                        date_time = ''
                        password_new=''
                        # Save Current Date in variable
                        date_time = str(datetime.datetime.now())
                        # Function - Calling  - With Return (Statement / Value) -  Generate Random Strong Password 
                        password_new = generate_random_strong_password_FUNCTION()   
                        print('The New Password Is:  ' , password_new)
                        # Save the Password in the variable
                        hash_pswd = make_password(password_new)
                        # Put the Password in the Field
                        current_user.password = hash_pswd 
                        # save the password in the database
                        current_user.save() 
                        #
                        # Send otp To Email - START
                        subject = "Welcome To Ecommerce Login!!"
                        # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to our Space!! \nThank you for visiting our website.\n We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n$p@r$h\nCEO of nothing"        
                        # message = "Hello " + user.first_name + "\n" + "One Time Password" + "\n" + "Code:  " +  otp +  "\n" + "Date/Time:  "  + str(datetime.datetime.now()) + "\n\nThanking You\nُemail@name.com\nThe Company's Name"        
                        message = "Hello " + current_user.first_name + "\n" + "One Time Password" + "\n" + "The New Password is:  " +  password_new +  "\n" + "Date:  "  + date_time + "\n" +"Passing the verification code for others exposes your account to the risk of fraud" + "\n\nThanking You\nُemail@name.com\nThe Company's Name"        
                        # the email we will be using to send it to teh the new user
                        from_email = settings.EMAIL_HOST_USER
                        # the user email
                        print("CURRENT USER EMAIL: " , current_user.email)
                        to_list = [current_user.email]
                        # fail_silently is used for the purpose that if teh email is not send, teh app should not crash 
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        # Send otp To Email - END
                        # messages when Password has been created in database
                        messages.success(request,'The New Password Has Been Sent To Email Successfully! Please LogIn.') # send Message to the user
                        return redirect('login_page-URL')
                    else:
                        messages.success(request,('User Is Not Active'))
                        return redirect('login_page-URL')
        else:
            messages.error(request, "EMAIL - The Entrance e-mail Is Not Registered With Us")
            return redirect('display_send_new_password_to_user-URL')
    else:
        return redirect('login_page-URL')
#
#
# Send The New Password To User Email
def send_new_password_to_user_email_DEF(request): # 
    # Verify that the data is protected
    if request.method == 'POST':
        # Receive user data
        email_insert_by_user = request.POST['send_new_password_to_user_email']
        # Verify the validity of the inputs - Email
        if not EMAIL_REGEX.match(email_insert_by_user):
            messages.error(request, "EMAIL - The Entrance e-mail Is Not Registered With Us")
            return redirect('display_send_new_password_to_user-URL')

        # Verify that the Email is not used by another user
        if User.objects.filter(email=email_insert_by_user).exists():
            messages.error(request, "Email - Congratulations, Your Email Has Been Verified In Our Records")

            # Search the user with the desired e -mail
            user_set = User.objects.filter(email=email_insert_by_user)
            # Get the user's object in all its methods and attributes
            userObj = user_set[0] # Save the user in the variable

            current_user = userObj # Save the user in the variable        
            # In the event that a user is found
            if current_user:
                    # If the user account is active
                    if current_user.is_active:
                        # Definition of variables
                        date_time = ''
                        password_new=''
                        # Save Current Date in variable
                        date_time = str(datetime.datetime.now())
                        # Function - Calling  - With Return (Statement / Value) -  Generate Random Strong Password 
                        password_new = FUNCTION_generate_random_strong_password()   
                        print('The New Password Is:  ' , password_new)
                        # Save the Password in the variable
                        hash_pswd = make_password(password_new)
                        # Put the Password in the Field
                        current_user.password = hash_pswd 
                        # save the password in the database
                        current_user.save() 
                        #
                        # Send otp To Email - START
                        subject = "Welcome To Ecommerce Login!!"
                        # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to our Space!! \nThank you for visiting our website.\n We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n$p@r$h\nCEO of nothing"        
                        # message = "Hello " + user.first_name + "\n" + "One Time Password" + "\n" + "Code:  " +  otp +  "\n" + "Date/Time:  "  + str(datetime.datetime.now()) + "\n\nThanking You\nُemail@name.com\nThe Company's Name"        
                        message = "Hello " + current_user.first_name + "\n" + "One Time Password" + "\n" + "The New Password is:  " +  password_new +  "\n" + "Date:  "  + date_time + "\n" +"Passing the verification code for others exposes your account to the risk of fraud" + "\n\nThanking You\nُemail@name.com\nThe Company's Name"        
                        # the email we will be using to send it to teh the new user
                        from_email = settings.EMAIL_HOST_USER
                        # the user email
                        print("CURRENT USER EMAIL: " , current_user.email)
                        to_list = [current_user.email]
                        # fail_silently is used for the purpose that if teh email is not send, teh app should not crash 
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        # Send otp To Email - END
                        # messages when Password has been created in database
                        messages.success(request,'The New Password Has Been Sent To Email Successfully! Please LogIn.') # send Message to the user
                        return redirect('login_page-URL')
                    else:
                        messages.success(request,('User Is Not Active'))
                        return redirect('login_page-URL')
        else:
            messages.error(request, "EMAIL - The Entrance e-mail Is Not Registered With Us")
            return redirect('display_send_new_password_to_user-URL')
    else:
        return redirect('login_page-URL')
#
#

# Send The New Password To User WhatsApp
def send_new_password_to_user_whatsapp_DEF(request): # 
    # Verify that the data is protected
    if request.method == 'POST':
        # Receive user data
        # # Save the current Mobile Number in var
        # filte_data_mobile_number_from_model  = SendOtpToWhatsappMODEL.objects.filter(SOTW_mobile_number=mobile_number_insert_by_user)
        # Save the current user
        # user = request.user
        # Save the current Mobile Number in var
        # table_mobile_number = SendOtpToWhatsappMODEL.objects.get(SOTW_user=user.id)

        # Receive user data
        email_insert_by_user                = request.POST.get('email_send_new_password_to_user_mobile')
        mobile_number_insert_by_user        = request.POST.get('mobile_send_new_password_to_user_mobile')

        # Verify the validity of the inputs - Email
        if not EMAIL_REGEX.match(str(email_insert_by_user)):
            messages.error(request, "EMAIL - The Entrance e-mail Is Not Registered With Us")
            return redirect('display_send_new_password_to_user-URL')

        # Verify that the Email is not used by another user
        if User.objects.filter(email=email_insert_by_user).exists():
            messages.error(request, "Email - Congratulations, Your Email Has Been Verified In Our Records")

        # Verify that the Email is not used by another user
        if SendOtpToWhatsappMODEL.objects.filter(SOTW_mobile_number=mobile_number_insert_by_user).exists():
            messages.error(request, "Mobile - Congratulations, Your Mobile Has Been Note Verified In Our Records")

        # Verify the validity of the inputs - UserName
        if not MOBIL_NUMBER_REGEX.match(str(mobile_number_insert_by_user)):
            messages.error(request, "Mobily Number - must be entered in the format: '+966000000000'.")
            return redirect('display_send_new_password_to_user-URL')

        # Verify the number of input letters
        if len(mobile_number_insert_by_user)!=13:
            messages.error(request, "Mobily Number must be Equal 13 Numbers")
            return redirect('display_send_new_password_to_user-URL')


        # Search the user with the desired e -mail
        # user_mobile_number = SendOtpToWhatsappMODEL.objects.get(SOTW_mobile_number=mobile_number_insert_by_user)
        # user_set = User.objects.filter(username=request.user.username)

            # Search the user with the desired e -mail
        user_set = User.objects.filter(email=email_insert_by_user)

        userObj = user_set[0] # Save the user in the variable
        current_user = userObj # Save the user in the variable        
        # In the event that a user is found
        if current_user:
                # If the user account is active
                if current_user.is_active:
                    # Entry to the system
                    # Definition of variables
                    date_time = ''
                    password_new=''
                    # Save Current Date in variable
                    date_time = str(datetime.datetime.now())
                    # Function - Calling  - With Return (Statement / Value) -  Generate Random Strong Password 
                    password_new = FUNCTION_generate_random_strong_password()   
                    print('The New Password Is:  ' , password_new)
                    # Save the Password in the variable
                    hash_pswd = make_password(password_new)
                    # Put the Password in the Field
                    current_user.password = hash_pswd 
                    # save the password in the database
                    current_user.save() 
                    ########################################################################
                    # Send Message To Whatsapp - START
                    user_mobile_number = SendOtpToWhatsappMODEL.objects.get(SOTW_mobile_number=mobile_number_insert_by_user)
                    # Verify that the WhatsApp service is active
                    # None:The Field Does Not Have Data - None = False
                    if user_mobile_number.SOTW_mobile_number is not None and user_mobile_number.SOTW_Is_whatsApp_active == True:
                        message = "\n" + "One Time Password" + "\n" + "       " + "                                 The New Password is: " +  password_new + "       " + "\n" + "                               Date: "  + date_time + "            " +"Passing the verification code for others exposes your account to the risk of fraud"        
                        # Message='User Account Created - We Thank You and welcome you to join us.'   
                        webbrowser.open('https://web.whatsapp.com/send?phone='+ str(user_mobile_number.SOTW_mobile_number) +'&text='+message)
                        time.sleep(10) # Seconds of stillness
                        pyautogui.press('enter') # Click on Inter key
                        # messages when Password has been created in database
                        messages.success(request,'The New Password Has Been Sent To WhatsApp Successfully! Please LogIn.') # send Message to the user
                        return redirect('login_page-URL')
                        # Send Message To Whatsapp - END
                    else:
                        messages.success(request,('User Is Not Active'))
                        return redirect('login_page-URL')
        else:
            messages.error(request, "EMAIL - The Entrance e-mail Is Not Registered With Us")
            return redirect('display_send_new_password_to_user-URL')
    else:
        return redirect('login_page-URL')
#
#