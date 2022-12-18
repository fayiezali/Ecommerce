from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from .models import UsersTable
#for password hashing
from django.contrib.auth.hashers import make_password, check_password
#for Regex (regular expression)
import re
from .models import Profile
# import requests (for google recaptcha)
# import requests
import json
import urllib
#for email sending
from django.conf import settings
import random
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail


# def change_password_DEF(request):
#     # password = request.POST.get('password')
#     # email    = request.POST.get('email')
#     password_v='W-@hot19_'
#     email_v='fayiez@hotmail.com'
#     user_set = User.objects.filter(email=email_v)
#     userObj = user_set[0]
#     print(userObj)
#     # Password encryption (make_password)
#     hash_pswd = make_password(password_v)
#     print(userObj.password)
#     userObj.password = hash_pswd
#     userObj.save()
#     messages.success(request,'Password Changed Successfully! Please LogIn.')
#     return render(request, 'dashboard/dashboard.html',{})


def change_password_DEF(request):
    email_v='fayiez@hotmail.com'
    user_set = User.objects.filter(email=email_v)
    userObj = user_set[0]

    if request.method == 'POST':
    # take all field entered by user so we cam work with them on backend
        password_old     = request.POST['pswd']
        password_new    = request.POST['npswd']
        password_confirm = request.POST['cnpswd']
#####################################
            #
        if password_old == password_new:
            messages.error(request , 'You cannot set old password as new password...')
            return redirect('changepassword-URL')
            # 
        if len(password_old)>20:
            messages.error(request, "password_old must be under 20 charcters!!")
            return redirect('changepassword-URL')
            #
        if len(password_old) ==0 or len(password_old) <=7 or len(password_old) =='':
            messages.error(request, "password_old -  The more than 8 characters, and must contain uppercase, number & symbol")
            return redirect('changepassword-URL')
            #
        if len(password_new) ==0 or len(password_new) <=7 or len(password_new) =='':
            messages.error(request, "password_new - The more than 8 characters, and must contain uppercase, number & symbol")
            return redirect('changepassword-URL')
            #
        if len(password_confirm) ==0 or len(password_confirm) <=7 or len(password_confirm) =='':
            messages.error(request, "password_confirm - The more than 8 characters, and must contain uppercase, number & symbol")
            return redirect('changepassword-URL')
            #
        if password_confirm != password_new:
            messages.success(request , 'Password & Confirm Password do not match!')
            return redirect('changepassword-URL')
#######################################
        if check_password(password_new, userObj.password):
            # validation
            pswdCriterian = {
            "length_criteria":".{8,}",
            "lowercase_criteria":"[a-z]+",
            "uppercase_criteria":"[A-Z]+",
            "number_criteria":"[0-9]+",
            "symbol_criteria":"[^A-Za-z0-9]+",
            }
            if not (re.search(pswdCriterian["length_criteria"], password_new) and re.search(pswdCriterian["lowercase_criteria"], password_new) and re.search(pswdCriterian["uppercase_criteria"], password_new) and re.search(pswdCriterian["number_criteria"], password_new) and re.search(pswdCriterian["symbol_criteria"], password_new)):
                messages.success(request , 'No - did not meet all required')
                return redirect('changepassword-URL')
############################
        # password_v=password_new
        # email_v='fayiez@hotmail.com'
        # user_set = User.objects.filter(email=email_v)
        # userObj = user_set[0]
        templatePath = "password_change/changepassword.html"
        # Password encryption (make_password)
        hash_pswd = make_password(password_new)
        print(userObj.password)
        userObj.password = hash_pswd
        userObj.save()
        messages.success(request,'Password Changed Successfully! Please LogIn.')
        return render(request, 'dashboard/dashboard.html',{})
    else:
        messages.success(request , 'No POST')    
        return render(request, 'password_change/changepassword.html',{})









# def change_password_DEF___(request):
#     # password = request.POST.get('password')
#     # email    = request.POST.get('email')
#     password_v='W-@hot19_'
#     email_v='fayiez@hotmail.com'
#     user_set = User.objects.filter(email=email_v)
#     userObj = user_set[0]
#     templatePath = "password_change/changepassword.html"
#     print(userObj)
    
#     # Password encryption (make_password)
#     hash_pswd = make_password(password_v)
#     print(userObj.password)
#     userObj.password = hash_pswd
#     userObj.save()
#     messages.success(request,'Password Changed Successfully! Please LogIn.')
#     return render(request, 'dashboard/dashboard.html',{})






























# def change_password_DEF____(request):
#     try:
#         input_email='fayiez@hotmail.com'
#         # input_email=''

#         if input_email:
#             # user_set = User.objects.filter(username = session['username'])
#             user_set = User.objects.filter(email = input_email)
#             userObj = user_set[0]
#             print("userObj")
#             templatePath = "password_change/changepassword.html"
#             # return render(request, 'password_change/changepassword.html',{})
#             try:
#                 if request.method == "POST":
#                     if "change_button" in request.POST:
#                         pswd = request.POST['pswd']
#                         npswd = request.POST['npswd']
#                         cnpswd = request.POST['cnpswd']
#                         context = {
#                             "formData": {
#                                 "pswd": pswd,
#                                 "npswd": npswd,
#                                 "cnpswd": cnpswd
#                             },
#                             "formErr": {}
#                         }
#                         # print(pswd,npswd,cnpswd,userObj.password)
#                         formErrorFlag = False
#                         print('step 01')
#                         # if check_password(pswd, userObj.password):
#                         #     #validation
#                         #     pswdCriterian = {
#                         #         "length_criteria":".{8,}",
#                         #         "lowercase_criteria":"[a-z]+",
#                         #         "uppercase_criteria":"[A-Z]+",
#                         #         "number_criteria":"[0-9]+",
#                         #         "symbol_criteria":"[^A-Za-z0-9]+",
#                         #     }
#                         #     if npswd == pswd:
#                         #         context['formErr']['npswdErr'] = "You cannot set old password as new password...."
#                         #         formErrorFlag = True
#                         #     else:
#                         #         if not(re.search(pswdCriterian["length_criteria"], npswd) and re.search(pswdCriterian["lowercase_criteria"], npswd) and re.search(pswdCriterian["uppercase_criteria"], npswd) and re.search(pswdCriterian["number_criteria"], npswd) and re.search(pswdCriterian["symbol_criteria"], npswd)):
#                         #             context['formErr']['npswdErr'] = "Please meet all password criterian...."
#                         #             formErrorFlag = True
#                         #         if cnpswd != npswd:
#                         #             print("Password & Confirm Password do not match!")
#                         #             context['formErr']['cnpswdErr'] = "New Password & Confirm New Password do not match!"
#                         #             formErrorFlag = True
#                         # else:
#                         #     print("not match")
#                         #     formErrorFlag = True
#                         #     context['formErr']['pswdErr'] = "Incorrect old password!"
                            
#                         if formErrorFlag:
#                             # templatePath = "password_change/changepassword.html"
#                             # response = render(request, templatePath, context)
#                             # return response
#                             context = {"successMsg": "The Entered Data Is Incorrect! In Addition, Try Again!"}
#                             return render(request, 'password_change/changepassword.html',{})
                            
#                         else:
#                             hash_pswd = make_password(npswd)
#                             print(userObj.password)
#                             userObj.password = hash_pswd
#                             userObj.save()
#                             context = {
#                                 "successMsg": "Password Changed Successfully!"
#                             }
#                             messages.success(request,'Password Changed Successfully! Please LogIn.')
#                             print("Changed")
#                             # templatePath = "dashboard/dashboard.html"
#                             # response = render(request, templatePath, context)
#                             # return response
#                             return render(request, 'dashboard/dashboard.html',context)
#             except Exception as e:
#                 print(e)
#             # context={}
#             # response = render(request, templatePath, context)
#             # return response
#             return render(request, 'password_change/changepassword.html',{})
#         else:
#             templatePath = "password_change/login_required.html"
#             response = render(request, templatePath)
#             print("step No Username")
#             return response
#             # return render(request, 'password_change/login_required.html',{})
#     except Exception as e:
#         # print(e)
#         # templatePath = "password_change/login_required.html"
#     # templatePath = "password_change/login_required.html"
#     # response = render(request, templatePath)
#     # return response
#         return render(request, 'password_change/login_required.html',{})

# PASSWARD_Criterian = {
#                     "length_criteria":".{8,}",
#                     "lowercase_criteria":"[a-z]+",
#                     "uppercase_criteria":"[A-Z]+",
#                     "number_criteria":"[0-9]+",
#                     "symbol_criteria":"[^A-Za-z0-9]+",
#                     }

# def _change_password_DEF(request):
    
#     input_email='fayiez@hotmail.com'
#     # input_email=''
#     if input_email:
#         user_set = User.objects.filter(email = input_email)
#         userObj = user_set[0]
#         print(userObj)
#         if request.method == 'POST':
#             # take all field entered by user so we cam work with them on backend
#             password_old     = request.POST['pswd']
#             password_new    = request.POST['npswd']
#             password_confirm = request.POST['cnpswd']
#             print(password_old)
#             print(password_new)
#             print(password_confirm)
#             # #
#             # if password_old == password_new:
#             #     messages.error(request , 'You cannot set old password as new password...')
#             #     return redirect('changepassword-URL')
#             # # 
#             # if len(password_old)>20:
#             #     messages.error(request, "password_old must be under 20 charcters!!")
#             #     return redirect('changepassword-URL')
#             # #
#             # if len(password_old) ==0 or len(password_old) <=7 or len(password_old) =='':
#             #     messages.error(request, "password_old -  The more than 8 characters, and must contain uppercase, number & symbol")
#             #     return redirect('changepassword-URL')
#             # #
#             # if len(password_new) ==0 or len(password_new) <=7 or len(password_new) =='':
#             #     messages.error(request, "password_new - The more than 8 characters, and must contain uppercase, number & symbol")
#             #     return redirect('changepassword-URL')
#             # #
#             # if len(password_confirm) ==0 or len(password_confirm) <=7 or len(password_confirm) =='':
#             #     messages.error(request, "password_confirm - The more than 8 characters, and must contain uppercase, number & symbol")
#             #     return redirect('changepassword-URL')
#             # #
#             # if password_confirm != password_new:
#             #     messages.success(request , 'Password & Confirm Password do not match!')
#             #     return redirect('changepassword-URL')

#             if check_password(password_old, userObj.password):
#             # validation
#                 pswdCriterian = {
#                 "length_criteria":".{8,}",
#                 "lowercase_criteria":"[a-z]+",
#                 "uppercase_criteria":"[A-Z]+",
#                 "number_criteria":"[0-9]+",
#                 "symbol_criteria":"[^A-Za-z0-9]+",
#                 }
#                 if (re.search(pswdCriterian["length_criteria"], password_new) and re.search(pswdCriterian["lowercase_criteria"], password_new) and re.search(pswdCriterian["uppercase_criteria"], password_new) and re.search(pswdCriterian["number_criteria"], password_new) and re.search(pswdCriterian["symbol_criteria"], password_new)):
#                     messages.success(request , '(Yes - All Required Has Been fulfilled ')
#                     return redirect('dashboard-URL')
#                 # messages.success(request , '(if check_password) - Yes -')    
#                 # return render(request, 'password_change/changepassword.html',{})
#             else:
#                 messages.success(request , 'No - did not meet all required ')    
#                 return render(request, 'password_change/changepassword.html',{})

            
#         else:
#             messages.success(request , 'No POST')    
#             return render(request, 'password_change/changepassword.html',{})
        
#     else:
#         messages.success(request , 'No User Data')
#         return render(request, 'password_change/login_required.html',{})

    