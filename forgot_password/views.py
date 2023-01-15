from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
# write a program to display the different random string method using the secrets.choice().  
# imports necessary packages  
import random   
import string  
import secrets  

def send_current_password_DEF(request):
    # Check the Post's use that hides the entered data
    if request.method == 'POST':
    # take all field entered by user so we cam work with them on backend
        # Search the user with the desired e -mail
                # Save the current user
        # user = request.user
        # Save the current Mobile Number in var
        # table_mobile_number = SendOtpToWhatsappMODEL.objects.get(SOTW_user=user.id)
        # user_set = request.user
        # userObj = user_set[0] # Save the user in the variable
        # current_password = userObj.username
        user = request.user
        # Save the current Mobile Number in var
        current_password = User.objects.get(username=user.username)
        # hash_pswd = make_password(current_password.password)
        # Save the password
        # userObj.password = hash_pswd # Save the Password in the variable

        print('Current Passwor:' ,  current_password.password)
        # 
        messages.success(request,'Send Current Password Successfully') # send Message to the user
        return render(request, 'forgot_password/send_current_password.html',{}) # Returen The Required HTML Page
    return render(request, 'forgot_password/send_current_password.html',{}) # Returen The Required HTML Page


# Display Authorization Web Page
def display_generate_random_strong_password_DEF(request):
    return render(request,'forgot_password/generate_random_strong_password.html', {})
#
# 
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


# Function - Defined - With Return (Statement / Value) - What The Job Is Doing:Generate Random Strong Password 
def generate_random_strong_password_FUNCTION(): 
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
    received_data = generate_random_strong_password_FUNCTION()    
    print( 'received_data', received_data )    
    messages.success(request , 'received_data: ' + str(received_data)) # send Message to the user
    return redirect('display_generate_random_strong_password-URL')

