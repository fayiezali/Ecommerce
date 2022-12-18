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



def change_password_DEF___(request):
    # password = request.POST.get('password')
    # email    = request.POST.get('email')
    password_v='W-@hot19_'
    email_v='fayiez@hotmail.com'
    user_set = User.objects.filter(email=email_v)
    userObj = user_set[0]
    templatePath = "password_change/changepassword.html"
    print(userObj)
    
    # Password encryption (make_password)
    hash_pswd = make_password(password_v)
    print(userObj.password)
    userObj.password = hash_pswd
    userObj.save()
    messages.success(request,'Password Changed Successfully! Please LogIn.')
    return render(request, 'dashboard/dashboard.html',{})


def change_password_DEF(request):
    try:
        email_v='fayiez@hotmail.com'
        # email_v=''

        if email_v:
            # user_set = User.objects.filter(username = session['username'])
            user_set = User.objects.filter(email = email_v)
            userObj = user_set[0]
            print("userObj")
            templatePath = "password_change/changepassword.html"
            # return render(request, 'password_change/changepassword.html',{})
            try:
                if request.method == "POST":
                    if "change_button" in request.POST:
                        pswd = request.POST['pswd']
                        npswd = request.POST['npswd']
                        cnpswd = request.POST['cnpswd']
                        context = {
                            "formData": {
                                "pswd": pswd,
                                "npswd": npswd,
                                "cnpswd": cnpswd
                            },
                            "formErr": {}
                        }
                        # print(pswd,npswd,cnpswd,userObj.password)
                        formErrorFlag = False
                        print('step 01')
                        # if check_password(pswd, userObj.password):
                        #     #validation
                        #     pswdCriterian = {
                        #         "length_criteria":".{8,}",
                        #         "lowercase_criteria":"[a-z]+",
                        #         "uppercase_criteria":"[A-Z]+",
                        #         "number_criteria":"[0-9]+",
                        #         "symbol_criteria":"[^A-Za-z0-9]+",
                        #     }
                        #     if npswd == pswd:
                        #         context['formErr']['npswdErr'] = "You cannot set old password as new password...."
                        #         formErrorFlag = True
                        #     else:
                        #         if not(re.search(pswdCriterian["length_criteria"], npswd) and re.search(pswdCriterian["lowercase_criteria"], npswd) and re.search(pswdCriterian["uppercase_criteria"], npswd) and re.search(pswdCriterian["number_criteria"], npswd) and re.search(pswdCriterian["symbol_criteria"], npswd)):
                        #             context['formErr']['npswdErr'] = "Please meet all password criterian...."
                        #             formErrorFlag = True
                        #         if cnpswd != npswd:
                        #             print("Password & Confirm Password do not match!")
                        #             context['formErr']['cnpswdErr'] = "New Password & Confirm New Password do not match!"
                        #             formErrorFlag = True
                        # else:
                        #     print("not match")
                        #     formErrorFlag = True
                        #     context['formErr']['pswdErr'] = "Incorrect old password!"
                            
                        if formErrorFlag:
                            # templatePath = "password_change/changepassword.html"
                            # response = render(request, templatePath, context)
                            # return response
                            context = {"successMsg": "The Entered Data Is Incorrect! In Addition, Try Again!"}
                            return render(request, 'password_change/changepassword.html',{})
                            
                        else:
                            hash_pswd = make_password(npswd)
                            print(userObj.password)
                            userObj.password = hash_pswd
                            userObj.save()
                            context = {
                                "successMsg": "Password Changed Successfully!"
                            }
                            messages.success(request,'Password Changed Successfully! Please LogIn.')
                            print("Changed")
                            # templatePath = "dashboard/dashboard.html"
                            # response = render(request, templatePath, context)
                            # return response
                            return render(request, 'dashboard/dashboard.html',context)
            except Exception as e:
                print(e)
            # context={}
            # response = render(request, templatePath, context)
            # return response
            return render(request, 'password_change/changepassword.html',{})
        else:
            templatePath = "password_change/login_required.html"
            response = render(request, templatePath)
            print("step No Username")
            return response
            # return render(request, 'password_change/login_required.html',{})
    except Exception as e:
        # print(e)
        # templatePath = "password_change/login_required.html"
    # templatePath = "password_change/login_required.html"
    # response = render(request, templatePath)
    # return response
        return render(request, 'password_change/login_required.html',{})




# changePassword function to change password
# def change_password_DEF(request,id):
#     if request.method == 'POST':
#         password = request.POST.get('password')
#         profile = Profile.objects.get(forget_password_token=id).user
#         user = User.objects.get(username = profile)
#         user.set_password(password)
#         user.save()
#         print(user.username)
#         print('change password',password)
#         messages.success(request,'Password Changed Successfully! Please LogIn.')
#         return redirect('login')
#     return render(request,'password_change/change-password.html')


# def change_password_DEF(request):
#     # password = request.POST.get('password')
#     # email    = request.POST.get('email')
#     password_v='f050A636@'
#     email_v='fayiez@hotmail.com'
#     User.objects.filter(email=email_v).update(password=password_v)
#     messages.success(request,'Password Changed Successfully! Please LogIn.')
#     return render(request, 'dashboard/dashboard.html',{})




# # changePassword function to change password
# def change_password_DEF(request,id):
#     if request.method == 'POST':
#         password = request.POST.get('password')
#         profile = Profile.objects.get(forget_password_token=id).user
#         user = User.objects.get(username = profile)
#         user.set_password(password)
#         user.save()
#         print(user.username)
#         print('change password',password)
#         messages.success(request,'Password Changed Successfully! Please LogIn.')
#         return redirect('login')
#     return render(request,'password_change/change-password.html')
    
    
    
    
    
    
    
    
    
# def change_password_DEF(request):
#     try:
#         # session = request.session
#         # if session['username']:
#         #     user_set = UsersTable.objects.filter(username = session['username'])
#         #     userObj = user_set[0]
        
#         # session = request.session
#         # if session['username']:
#         #     user_set = User.objects.filter(username = session['username'])
#         #     userObj = user_set[0]
#         session = request.session
#         if session['username']:
#             user_set = User.objects.filter(username = session['username'])
#             userObj = user_set[0]
#             print("userObj")
#             templatePath = "password_change/changepassword.html"
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
#                         print(pswd,npswd,cnpswd,userObj.password)
#                         formErrorFlag = False
#                         print('step 01')
#                         if check_password(pswd, userObj.password):
#                             #validation
#                             pswdCriterian = {
#                                 "length_criteria":".{8,}",
#                                 "lowercase_criteria":"[a-z]+",
#                                 "uppercase_criteria":"[A-Z]+",
#                                 "number_criteria":"[0-9]+",
#                                 "symbol_criteria":"[^A-Za-z0-9]+",
#                             }
#                             if npswd == pswd:
#                                 context['formErr']['npswdErr'] = "You cannot set old password as new password...."
#                                 formErrorFlag = True
#                             else:
#                                 if not(re.search(pswdCriterian["length_criteria"], npswd) and re.search(pswdCriterian["lowercase_criteria"], npswd) and re.search(pswdCriterian["uppercase_criteria"], npswd) and re.search(pswdCriterian["number_criteria"], npswd) and re.search(pswdCriterian["symbol_criteria"], npswd)):
#                                     context['formErr']['npswdErr'] = "Please meet all password criterian...."
#                                     formErrorFlag = True
#                                 if cnpswd != npswd:
#                                     print("Password & Confirm Password do not match!")
#                                     context['formErr']['cnpswdErr'] = "New Password & Confirm New Password do not match!"
#                                     formErrorFlag = True
#                         else:
#                             print("not match")
#                             formErrorFlag = True
#                             context['formErr']['pswdErr'] = "Incorrect old password!"
                            
#                         if formErrorFlag:
#                             templatePath = "password_change/changepassword.html"
#                             response = render(request, templatePath, context)
#                             return response
#                         else:
#                             hash_pswd = make_password(npswd)
#                             print(userObj.password)
#                             userObj.password = hash_pswd
#                             userObj.save()
#                             context = {
#                                 "successMsg": "Password Changed Successfully!"
#                             }
#                             print("Changed")
#                             templatePath = "password_change/changepassword.html"
#                             response = render(request, templatePath, context)
#                             return response
#             except Exception as e:
#                 print(e)
#             context={}
#             response = render(request, templatePath, context)
#             return response
#         else:
#             templatePath = "password_change/login_required.html"
#             response = render(request, templatePath)
#             print("step No Username")
#             return response
#     except Exception as e:
#         print(e)
#         templatePath = "password_change/login_required.html"
#     templatePath = "password_change/login_required.html"
#     response = render(request, templatePath)
#     return response

