from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User # إستيراد اسم المستخدم
#for password hashing
from django.contrib.auth.hashers import make_password, check_password
#for Regex (regular expression)
#for email sending
from django.conf import settings
import random
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail

def change_password_DEF(request):
    # Check the Post's use that hides the entered data
    if request.method == 'POST':
    # take all field entered by user so we cam work with them on backend
        password_old     = request.POST['curent_password']      # Curnet password
        password_new    = request.POST['new_password']        # New password    
        password_confirm = request.POST['confirm_new_password'] # Confirm new password
        user_email       = request.POST['email']               # Email
        # Search the user with the desired e -mail
        user_set = User.objects.filter(email=user_email)
        userObj = user_set[0] # Save the user in the variable
        # New Password - Verify the authenticity of the entered data
        if password_new.isnumeric() and password_new.islower() and  password_new.isalnum() and  password_new.isalpha() and  password_new.isdigit() and  password_new.isupper():
            messages.error(request, "The Password must contain numeric & characters & lowercase & uppercase & symbol")
            return redirect('changepassword-URL')
        # Ole Password - Verify the authenticity of the entered data
        if password_old == password_new:
            messages.error(request , 'You cannot set old password as new password...')
            return redirect('changepassword-URL')
        # Old Password - Verify the authenticity of the entered data
        if len(password_old)>20:
            messages.error(request, "password_old must be under 20 charcters!!")
            return redirect('changepassword-URL')
        # Old Password - Verify the authenticity of the entered data
        if len(password_old) ==0 or len(password_old) <=7 or len(password_old) =='':
            messages.error(request, "password_old -  The more than 8 characters, and must contain uppercase, number & symbol")
            return redirect('changepassword-URL')
        # New Password - Verify the authenticity of the entered data
        if len(password_new) ==0 or len(password_new) <=7 or len(password_new) =='':
            messages.error(request, "password_new - The more than 8 characters, and must contain uppercase, number & symbol")
            return redirect('changepassword-URL')
        # Confirm Password - Verify the authenticity of the entered data
        if len(password_confirm) ==0 or len(password_confirm) <=7 or len(password_confirm) =='':
            messages.error(request, "password_confirm - The more than 8 characters, and must contain uppercase, number & symbol")
            return redirect('changepassword-URL')
        # Confirm Password - Verify the authenticity of the entered data
        if password_confirm != password_new:
            messages.success(request , 'Password & Confirm Password do not match!')
            return redirect('changepassword-URL')
        # Password encryption By (make_password)
        hash_pswd = make_password(password_new)
        # Save the password
        userObj.password = hash_pswd # Save the Password in the variable
        userObj.save() # save the password in the database
        messages.success(request,'Password Changed Successfully! Please LogIn.') # send Message to the user
        return render(request, 'dashboard/dashboard.html',{}) # Returen The Required HTML Page
    else:
        # messages.success(request , 'No POST')    
        return render(request, 'password_change/changepassword.html',{})
